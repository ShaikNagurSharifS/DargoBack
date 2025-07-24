from architech.app.models.user import User
import json
import os


# In-memory user store for demo. Replace with DB logic.
users = {}

def get_user_by_username(username: str):
    user = users.get(username)
    if user:
        return user
    # If not found in memory, check userdata.json
    try:
        USERDATA_PATH = os.path.join(os.path.dirname(__file__), '../../userdata.json')
        with open(USERDATA_PATH, "r") as f:
            data = json.load(f)
        user_data = data.get(username)
        if user_data:
            # Recreate User object from dict
            return User(**user_data)
    except (FileNotFoundError, json.JSONDecodeError):
        pass
    return None

def get_user_info(username: str):

    try:
        with open(USERDATA_PATH, "r") as f:
            data = json.load(f)
        user = data.get(username)
        if user:
            return {"username": user.get("username"), "role": user.get("role")}
        else:
            return None
    except (FileNotFoundError, json.JSONDecodeError):
        return None


USERDATA_PATH = os.path.join(os.path.dirname(__file__), '../../userdata.json')

def create_user(username: str, email: str, password_hash: str, role: str):
    user = User(username=username, email=email, password_hash=password_hash, role=role)
    user_dict = user.dict()
    user_dict["role"] = role
    users[username] = user
    # Load existing data
    try:
        with open(USERDATA_PATH, "r") as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        data = {}
    data[username] = user_dict
    with open(USERDATA_PATH, "w") as f:
        json.dump(data, f, indent=2)
    return user
