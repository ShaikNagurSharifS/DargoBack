def resolve_user(user_id: int):
    # TODO: Replace with DB/service call
    if user_id == 1:
        return {"id": 1, "name": "Nagur", "email": "nagur@example.com"}
    return None

def create_user(name: str, email: str):
    # TODO: Replace with DB/service call
    return {"id": 2, "name": name, "email": email}
