
import json
import os
import hashlib

FILE = "users.json"


# Create JSON file if it doesn't exist
if not os.path.exists(FILE):
    with open(FILE, "w") as f:
        json.dump([], f)


# Hash password
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


# Read users
def get_users():
    with open(FILE, "r") as f:
        return json.load(f)


# Register user
def create_user(username, email, password):

    users = get_users()

    # Check existing email
    for user in users:
        if user["email"] == email:
            return False

    new_user = {
        "username": username,
        "email": email,
        "password": hash_password(password)
    }

    users.append(new_user)

    with open(FILE, "w") as f:
        json.dump(users, f, indent=4)

    return True


# Login verification
def verify_user(email, password):

    users = get_users()
    hashed_password = hash_password(password)

    for user in users:
        if (user["email"] == email and
                user["password"] == hashed_password):

            return user["username"]

    return None
