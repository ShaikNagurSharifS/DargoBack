from pydantic import BaseModel

class User(BaseModel):
    username: str
    email: str
    password_hash: str
    role:str  # e.g., "user", "admin"
    # Add more fields as needed

class UserRegister(BaseModel):
    username: str
    password: str
    confirm_password: str
    email: str
    role: str


class UserLogin(BaseModel):
    username: str
    password: str
    role: str
