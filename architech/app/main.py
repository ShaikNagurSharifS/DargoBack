from fastapi import FastAPI, Query, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from architech.app.config.settings import OAUTH2_TOKEN_URL, ALGORITHM, SECRET_KEY

# In-memory session secret storage: {username: secret_key}
session_secrets = {}

import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')
from time import time
import getpass
import os

from architech.app.services.user_service import get_user_info
from architech.app.vroute.flag_routes import feature_flags
from architech.app.auth.pass_hash import hash_password, verify_password
from architech.app.auth.jwt_handler import create_access_token
from architech.app.services.user_service import get_user_by_username, create_user
from architech.app.models.user import UserRegister, UserLogin  # Corrected import for user schemas

from fastapi import FastAPI
from architech.app.config.openapi import custom_openapi

app = FastAPI()
app.openapi = lambda: custom_openapi(app)
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # or ["*"] for all origins (not recommended for production)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl=OAUTH2_TOKEN_URL)

def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        import logging
        logging.info(f"Validating JWT token: {token}")
        from jose import jwt
        unverified_payload = jwt.get_unverified_claims(token)
        username = unverified_payload.get("sub")
        role = unverified_payload.get("role")
        if username is None or role is None:
            logging.warning(f"JWT missing username or role: username={username}, role={role}")
            raise credentials_exception
    except JWTError as e:
        logging.error(f"JWTError during token validation: {str(e)}")
        raise credentials_exception
    return {"username": username, "role": role}

start_time = time()


from fastapi.responses import JSONResponse

def api_success(data=None, message="Success", status_code=200):
    return JSONResponse(content={"success": True, "message": message, "data": data}, status_code=status_code)

def api_error(message="Error", status_code=400, detail=None):
    return JSONResponse(content={"success": False, "message": message, "detail": detail}, status_code=status_code)

@app.get("/", tags=["Root"])
def read_root():
    starter = os.environ.get("APP_STARTER") or getpass.getuser() or "there"
    return api_success({"message": f"Hello, {starter}!"})

@app.get("/greet", tags=["Greet"])
def greet(name: str = "Guest", title: str = None):
    try:
        greeting = f"Hello, {title + ' ' if title else ''}{name}!"
        return api_success({"greeting": greeting})
    except Exception as e:
        return api_error("Failed to greet", 500, str(e))

@app.get("/greet/{name}", tags=["Greet"])
def greet_path(name: str, title: str = None):
    try:
        greeting = f"Hello, {title + ' ' if title else ''}{name}!"
        return api_success({"greeting": greeting})
    except Exception as e:
        return api_error("Failed to greet", 500, str(e))

try:
    import psutil
except ImportError:
    psutil = None

@app.get("/metrics/performance", tags=["Metrics"])
def performance_metrics():
    try:
        if not psutil:
            return api_error("psutil not installed. Run 'pip install psutil' for performance metrics.", 500)
        mem = psutil.virtual_memory()
        cpu = psutil.cpu_percent(interval=0.1)
        return api_success({
            "memory_total_mb": round(mem.total / 1024 / 1024, 2),
            "memory_used_mb": round(mem.used / 1024 / 1024, 2),
            "memory_percent": mem.percent,
            "cpu_percent": cpu
        })
    except Exception as e:
        return api_error("Failed to get performance metrics", 500, str(e))

@app.get("/health", tags=["Health"])
def health_check():
    try:
        return api_success({"status": "ok"})
    except Exception as e:
        return api_error("Health check failed", 500, str(e))

@app.get("/metrics/uptime", tags=["Metrics"])
def uptime():
    try:
        return api_success({"uptime_seconds": round(time() - start_time, 2)})
    except Exception as e:
        return api_error("Failed to get uptime", 500, str(e))

@app.get("/metrics/system", tags=["Metrics"])
def system_info():
    try:
        import platform
        uname = platform.uname()
        return api_success({
            "hostname": uname.node,
            "user": getpass.getuser(),
            "os": uname.system,
            "release": uname.release,
            "version": uname.version
        })
    except Exception as e:
        return api_error("Failed to get system info", 500, str(e))

@app.get("/metrics/environment", tags=["Metrics"])
def environment_info(): 
    try:
        env_vars = {key: value for key, value in os.environ.items() if key.startswith("APP_") or key.startswith("ARCHITECH_")}
        return api_success(env_vars)
    except Exception as e:
        return api_error("Failed to get environment info", 500, str(e))


logger = logging.getLogger("featureflags")

@app.get("/feature_flags", tags=["Feature Flags"])
def get_feature_flags(
    user_type: str = Query(None, alias="user_type", description="User type to filter feature flags")
):
    try:
        flags = feature_flags(user_type=user_type)
        return api_success(flags)
    except Exception as e:
        logger.error(f"Feature flag error: {str(e)}", exc_info=True)
        return api_error("Failed to get feature flags", 500, str(e))

# --- Auth Endpoints ---
@app.post("/auth/register", tags=["Auth"])
def register(user: UserRegister):
    try:
        existing = get_user_by_username(user.username)
        if existing:
            return api_error("Username already exists", 400)
        if user.password != user.confirmpassword:
            return api_error("Passwords do not match", 400)
        hashed_pw = hash_password(user.password)
        new_user = create_user(username=user.username, email=user.email, password_hash=hashed_pw, role=user.role)
        return api_success({"username": new_user.username, "email": new_user.email, "role": new_user.role}, "User registered successfully")
    except Exception as e:
        return api_error("Registration failed", 500, str(e))

from fastapi import HTTPException

@app.post("/auth/login", tags=["Auth"])
def login(user: UserLogin):
    try:
        db_user = get_user_by_username(user.username)
        logging.info(f"Login attempt: username={user.username}, password={user.password}, role={user.role}")
        if db_user:
            logging.info(f"Stored user: username={db_user.username}, password_hash={db_user.password_hash}, role={getattr(db_user, 'role', db_user.dict().get('role', None))}")
        if not db_user:
            logging.warning(f"Login failed: user '{user.username}' not found.")
            raise HTTPException(status_code=401, detail="User not found")
        if not verify_password(user.password, db_user.password_hash):
            logging.warning(f"Login failed: wrong password for user '{user.username}'. Provided password: {user.password}, Stored hash: {db_user.password_hash}")
            raise HTTPException(status_code=401, detail="Incorrect password")
        # Role check
        if hasattr(db_user, "role"):
            stored_role = getattr(db_user, "role", None)
        else:
            stored_role = db_user.dict().get("role") if db_user else None
        if user.role != stored_role:
            logging.warning(f"Role mismatch for user: {user.username}. Provided: {user.role}, Stored: {stored_role}")
            raise HTTPException(status_code=401, detail="Invalid role for user")
        token = create_access_token({"sub": db_user.username, "role": stored_role})
        return api_success({"access_token": token, "token_type": "bearer", "role": stored_role}, "Login successful")
    except HTTPException as e:
        raise e
    except Exception as e:
        return api_error("Login failed", 500, str(e))

# --- User Profile Endpoint ---
@app.get("/user/profile", tags=["User"])
def user_profile(current_user: dict = Depends(get_current_user)):
    try:
        info = get_user_info(current_user["username"])
        if not info:
            return api_error("User not found", 404)
        db_user = get_user_by_username(current_user["username"])
        email = getattr(db_user, "email", None) if db_user else None
        return api_success({"username": info["username"], "role": info["role"], "email": email})
    except Exception as e:
        return api_error("Failed to get user profile", 500, str(e))

# --- Role-based Feature Flags Endpoint ---
@app.get("/user/featureflags", tags=["User"])
def user_featureflags(current_user: dict = Depends(get_current_user)):
    try:
        info = get_user_info(current_user["username"])
        if not info:
            return api_error("User not found", 404)
        role = info["role"]
        flags = feature_flags(user_type=role)
        return api_success({
            "username": info["username"],
            "role": role,
            "feature_flags": flags if isinstance(flags, dict) else {"error": "No feature flags found"}
        })
    except Exception as e:
        import logging
        logging.error(f"Error in /user/featureflags: {str(e)}", exc_info=True)
        return api_error("Failed to get user feature flags", 500, str(e))

## ...existing code...
