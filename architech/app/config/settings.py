import os

OAUTH2_TOKEN_URL = os.getenv("OAUTH2_TOKEN_URL", "/auth/login")
ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")
SECRET_KEY = os.getenv("JWT_SECRET")
