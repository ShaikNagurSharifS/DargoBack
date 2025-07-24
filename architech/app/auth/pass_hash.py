import hashlib
import hmac

SECRET_KEY = b"your-secret-key"  # Change this in production

def hash_password(password: str) -> str:
    return hmac.new(SECRET_KEY, password.encode(), hashlib.sha256).hexdigest()

def verify_password(password: str, password_hash: str) -> bool:
    return hmac.new(SECRET_KEY, password.encode(), hashlib.sha256).hexdigest() == password_hash
