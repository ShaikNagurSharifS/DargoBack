# Feature Flags Implementation Guide

## Overview
This project implements a flexible feature flag system for controlling UI components, permissions, and access based on user type (admin, user, guest, etc.). Feature flags are managed via a JSON file and exposed through FastAPI endpoints for dynamic frontend/backend integration.

---

## File Structure & Locations

- **Feature Flags Data**
  - `architech/shared/code_rules/feature_flags.json`
    - Stores all feature flag definitions for each user type.
    - Example structure:
      ```json
      {
        "admin": { ... },
        "user": { ... },
        "guest": { ... },
        "string": { "additionalProp1": "Sorry you are not a Trusted User" }
      }
      ```

- **Feature Flag Loader & API Logic**
  - `architech/core/feature_flags.py`
    - Functions to load all flags and get flags for a specific user type.
    - Used by API routes to fetch flag data.

- **API Route**
  - `architech/app/vroute/flag_routes.py`
    - Defines the `feature_flags` function for the endpoint.
    - Handles query parameter, validates user type, and returns appropriate flag data or error message.

- **Main API Registration**
  - `architech/app/main.py`
    - Registers the `/feature_flags` endpoint and delegates to `flag_routes.py`.

---


## How It Works

1. **Feature Flag Data**
   - All flags are defined in `feature_flags.json`.
   - Each user type (admin, user, guest) has its own set of flags (navbar, sections, permissions).
   - A special `string` entry provides a fallback message for unrecognized user types.

2. **Backend Logic & Exception Handling**
   - The API endpoint `/feature_flags` accepts a `user_type` query parameter.
   - If `user_type` is missing, returns `{ "error": "Please enter user" }`.
   - If `user_type` matches a key in the JSON, returns those flags.
   - If not, returns the fallback message from the `string` entry.
   - All feature flag access is wrapped in try/except blocks for robust error handling.
   - Errors are logged using Python's `logging` module for enterprise-grade monitoring.
   - Example error response: `{ "error": "Feature flag error: [details]" }`

3. **Usage Example**
   - **Request:** `GET /feature_flags?user_type=admin`
   - **Response:** Returns all admin flags.
   - **Request:** `GET /feature_flags?user_type=unknown`
   - **Response:** `{ "additionalProp1": "Sorry you are not a Trusted User" }`
   - **Request:** `GET /feature_flags` (no user_type)
   - **Response:** `{ "error": "Please enter user" }`

---

## Extending Feature Flags
- Add new user types or flags by editing `feature_flags.json`.
- Update backend logic in `flag_routes.py` if you need custom validation, fallback behavior, or advanced error handling.
- Frontend can dynamically render UI based on the flags returned from the API.

---

## Best Practices
- Keep `feature_flags.json` up to date with all possible roles and permissions.
- Use the fallback message for security and user experience.
- Document any changes to flag structure for frontend/backend teams.
- Always use try/except blocks for file and JSON operations.
- Log errors for monitoring and debugging.
- Consider automated tests for error scenarios.

---

## Authentication & Security

To protect feature flag endpoints and ensure only authorized users access sensitive flags:

1. **Use JWT Authentication**
   - Implement login endpoints that issue JWT tokens after verifying credentials.
   - Store only hashed passwords using secure algorithms.
   - Example: Use `architech/app/auth/jwt_handler.py` and `pass_hash.py` for token and password management.

2. **Protect Endpoints**
   - Require authentication for `/feature_flags` and other sensitive routes using FastAPI's `Depends`.
   - Example:
     ```python
     from fastapi import Depends, HTTPException, status
     from architech.app.auth.jwt_handler import verify_jwt

     def get_current_user(token: str = Depends(oauth2_scheme)):
         user = verify_jwt(token)
         if not user:
             raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
         return user

     @app.get("/feature_flags")
     def get_flags(current_user=Depends(get_current_user)):
         # ...existing flag logic...
     ```

3. **Role-Based Access**
   - Include user roles in JWT payloads and check roles in endpoints to restrict access (e.g., admin-only flags).

4. **Frontend Integration**
   - Send JWT in the `Authorization` header: `Bearer <token>`.
   - Store tokens securely (prefer HTTP-only cookies for web apps).

5. **Exception Handling & Logging**
   - Always wrap authentication logic in try/except blocks.
   - Log authentication errors for monitoring and debugging.

6. **Testing**
   - Write automated tests for login, token validation, and protected endpoints.

---

## Contact
For questions or improvements, contact the backend team or refer to this README for integration details.
