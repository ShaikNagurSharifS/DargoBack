# DargoBack

## Project Structure

```
DargoBack/
├── .env
├── .git/
├── .gitignore
├── alembic/
│   └── __init__.py
├── architech/
│   ├── app/
│   │   ├── vroute/
│   │   │   ├── graph_routes.py
│   │   │   ├── rest_routes.py
│   │   │   └── __init__.py
│   │   └── __init__.py
│   ├── auth/
│   │   ├── jwt_handler.py
│   │   ├── pass_hash.py
│   │   ├── permissions.py
│   │   └── __init__.py
│   ├── core/
│   │   ├── config.py
│   │   ├── feature_flags.py
│   │   ├── privacy.py
│   │   ├── security.py
│   │   └── __init__.py
│   ├── dbase/
│   │   ├── base.py
│   │   ├── db_seed.py
│   │   ├── mbase.py
│   │   ├── models/
│   │   │   ├── user.py
│   │   │   └── __init__.py
│   │   ├── pbase.py
│   │   ├── repos/
│   │   │   ├── user_repo.py
│   │   │   └── __init__.py
│   │   └── __init__.py
│   ├── graphql/
│   │   ├── queries/
│   │   │   ├── uer_query.py
│   │   │   └── __init__.py
│   │   ├── resolvers/
│   │   │   ├── user_mutation.py
│   │   │   └── __init__.py
│   │   ├── schema.py
│   │   └── __init__.py
│   ├── infra/
│   │   ├── cache.py
│   │   ├── email.py
│   │   ├── storage.py
│   │   └── __init__.py
│   ├── middleman/
│   │   ├── auth_man.py
│   │   ├── logging.py
│   │   └── __init__.py
│   ├── schemas/
│   │   ├── scheme_auth.py
│   │   ├── scheme_user.py
│   │   └── __init__.py
│   ├── services/
│   │   ├── user_service.py
│   │   └── __init__.py
│   ├── shared/
│   │   ├── code_rules/
│   │   │   ├── feature_flags.json
│   │   │   ├── regex_patterns.py
│   │   │   ├── response_codes.py
│   │   │   ├── validation_rules.py
│   │   │   └── __init__.py
│   │   ├── constants/
│   │   │   ├── constants.py
│   │   │   ├── enums.py
│   │   │   └── __init__.py
│   │   ├── Exceptions/
│   │   │   ├── custom_errors.py
│   │   │   ├── handlers.py
│   │   │   └── __init__.py
│   │   └── __init__.py
│   ├── sockets/
│   │   ├── chat_sock.py
│   │   ├── notification_sock.py
│   │   └── __init__.py
│   ├── utils/
│   │   ├── common.py
│   │   ├── hashing.py
│   │   ├── logger.py
│   │   ├── response_wrapper.py
│   │   └── __init__.py
│   ├── webhooks/
│   │   ├── generic_whooks.py
│   │   ├── payment_whooks.py
│   │   └── __init__.py
│   └── __init__.py
├── docker-compose.yml
├── Dockerfile
├── README.md
├── tests/
│   ├── api/
│   ├── db/
│   ├── test_auth.py
│   ├── test_graphql.py
│   ├── test_users.py
│   └── __init__.py
```

This structure provides a clear overview of all files and folders in the project for easy navigation and understanding.
## Folder and File Purpose

- **.env**: Environment variables for configuration (e.g., secrets, database URLs).
- **.git/**: Git version control metadata.
- **.gitignore**: Specifies files and folders to be ignored by Git.
- **alembic/**: Database migrations (managed by Alembic).
  - `__init__.py`: Marks the folder as a Python package.
- **architech/**: Main application source code, organized by domain and responsibility.
  - **app/**: Application entry points and route definitions.
    - **vroute/**: Contains route handlers for GraphQL and REST APIs.
  - **auth/**: Authentication, password hashing, permissions, and JWT handling.
  - **core/**: Core configuration, feature flags, privacy, and security logic.
  - **dbase/**: Database models, base classes, and repository patterns.
    - **models/**: ORM models (e.g., user.py).
    - **repos/**: Data access and repository logic.
  - **graphql/**: GraphQL schema, queries, and resolvers.
    - **queries/**: GraphQL query definitions.
    - **resolvers/**: GraphQL mutation and resolver logic.
  - **infra/**: Infrastructure services (caching, email, storage).
  - **middleman/**: Middleware for authentication and logging.
  - **schemas/**: Pydantic or Marshmallow schemas for data validation.
  - **services/**: Business logic and service layer (e.g., user_service.py).
  - **shared/**: Shared resources and utilities.
    - **code_rules/**: Validation rules, regex patterns, response codes, feature flags.
      - `feature_flags.json`: JSON file defining feature toggles for the application.
      - `regex_patterns.py`: Common regular expressions for validation and parsing.
      - `response_codes.py`: Standardized API response codes and messages.
      - `validation_rules.py`: Centralized validation logic for input data.
    - **constants/**: Project-wide constants and enums.
      - `constants.py`: Frequently used constant values across the project.
      - `enums.py`: Enumerations for fixed sets of values.
    - **Exceptions/**: Custom error classes and handlers.
      - `custom_errors.py`: User-defined exception classes for error handling.
      - `handlers.py`: Functions to handle and format exceptions.
  - **sockets/**: WebSocket handlers for chat and notifications.
  - **utils/**: Utility functions (logging, hashing, response wrappers).
    - `common.py`: Miscellaneous helper functions used throughout the codebase.
    - `hashing.py`: Functions for hashing passwords and other sensitive data.
    - `logger.py`: Logging setup and helper functions for consistent logging.
    - `response_wrapper.py`: Standardized API response formatting utilities.
  - **webhooks/**: Webhook handlers (e.g., payment, generic events).
  - `__init__.py`: Marks the folder as a Python package.
- **docker-compose.yml**: Docker Compose configuration for multi-container setups.
- **Dockerfile**: Docker build instructions for the application.
- **README.md**: Project documentation and structure.
- **tests/**: Unit and integration tests.
  - **api/**: (Empty) Placeholder for API-related tests.
  - **db/**: (Empty) Placeholder for database-related tests.
  - `test_auth.py`: Tests for authentication features.
  - `test_graphql.py`: Tests for GraphQL endpoints.
  - `test_users.py`: Tests for user-related features.
  - `__init__.py`: Marks the folder as a Python package.

---

## Getting Started

## How to Run Locally

1. (Optional) Create and activate a virtual environment:
   ```sh
   python -m venv venv
   .\venv\Scripts\activate  # On Windows
   source venv/bin/activate  # On Linux/Mac
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Copy `.env.example` to `.env` and fill in any required environment variables.
4. Run database migrations (if needed):
   ```sh
   alembic upgrade head
   ```
5. Start the FastAPI app:
   ```sh
   uvicorn architech.app.main:app --reload
   ```
6. Open your browser and go to [http://localhost:8000](http://localhost:8000) to see the API.
7. For the interactive API docs, visit [http://localhost:8000/docs](http://localhost:8000/docs)

1. **Clone the repository:**
   ```sh
   git clone <repo-url>
   cd DargoBack
   ```
2. **Set up your environment:**
   - Copy `.env.example` to `.env` and fill in required values (if applicable).
   - (Optional) Create and activate a Python virtual environment:
     ```sh
     python -m venv venv
     .\venv\Scripts\activate  # On Windows
     source venv/bin/activate  # On Linux/Mac
     ```
3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
4. **Run database migrations:**
   ```sh
   alembic upgrade head
   ```
5. **Start the application (development):**
   ```sh
   uvicorn architech.app.main:app --reload
   ```

## Production Ready

For production, use gunicorn with uvicorn workers:

```sh
gunicorn architech.app.main:app -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000 --workers 4
```

You can adjust the number of workers based on your server's CPU cores.

## How to Run Tests

```sh
pytest tests/
```

## Project Flow (High-Level)

1. **Request Handling:**
   - HTTP/GraphQL/WebSocket requests enter via routes in `architech/app/vroute/`.
2. **Authentication & Middleware:**
   - Requests pass through authentication and logging middleware (`architech/middleman/`).
3. **Business Logic:**
   - Core logic is handled in `architech/services/` and validated with schemas in `architech/schemas/`.
4. **Database Access:**
   - Data is accessed and persisted using models and repositories in `architech/dbase/`.
5. **Response:**
   - Responses are formatted and returned, possibly using helpers in `architech/utils/` and `architech/shared/`.

---

For more details, see comments in the code or reach out to the maintainers.

---

## Dependencies & Packages: Why, What, When, How

### How to Run

1. Activate your virtual environment (if using one):
   ```sh
   .\venv\Scripts\activate  # On Windows
   source venv/bin/activate  # On Linux/Mac
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Start the FastAPI app (development):
   ```sh
   uvicorn architech.app.main:app --reload
   ```
4. For production, use gunicorn:
   ```sh
   gunicorn architech.app.main:app -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000 --workers 4
   ```

This project uses several Python packages to provide web, database, and utility functionality. Here’s a quick guide:

### Why
- To avoid reinventing the wheel and use robust, community-tested solutions for web APIs, database access, authentication, etc.

### What (Common Packages)
- **fastapi**: Main web framework for building APIs (async, modern, type-safe).
- **uvicorn**: ASGI server to run FastAPI apps in development/production.
- **alembic**: Database migrations (schema changes over time).
- **sqlalchemy**: ORM for database models and queries.
- **pydantic**: Data validation and settings management.
- **python-dotenv**: Loads environment variables from .env files.
- **python-multipart**: Handles file uploads in FastAPI.
- **passlib**: Password hashing utilities.
- **prometheus-client**: Exposes metrics for monitoring (use this, not `prometheus`).
- **pytest**: Testing framework.

### When
- Install all dependencies before running the app: `pip install -r requirements.txt`
- Add new packages when you need extra features (e.g., JWT auth, CORS, metrics, etc.).
- Update packages regularly for security and bug fixes.

### How
1. **To install all dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
2. **To add a new package:**
   ```sh
   pip install <package-name>
   pip freeze > requirements.txt
   ```
3. **To update a package:**
   ```sh
   pip install --upgrade <package-name>
   pip freeze > requirements.txt
   ```
4. **To remove a package:**
   - Uninstall: `pip uninstall <package-name>`
   - Update requirements: `pip freeze > requirements.txt`

### Example: Adding Prometheus Metrics
If you want to expose metrics for monitoring:
```sh
pip install prometheus-client
```
Then use it in your FastAPI app as shown in the [prometheus-client documentation](https://github.com/prometheus/client_python).

---