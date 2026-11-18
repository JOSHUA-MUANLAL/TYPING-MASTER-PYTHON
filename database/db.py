
import json
import hashlib
from pathlib import Path

# Location of users.json
FILE = Path(__file__).resolve().parent.parent / "users.json"


# Create file if it doesn't exist
if not FILE.exists():
    FILE.write_text("[]")


# Convert password into a hash
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


# Read all users
def get_users():
    with open(FILE, "r") as file:
        return json.load(file)


# Register a new user
def create_user(username, email, password):

    users = get_users()

    # Check if email already exists
    for user in users:
        if user["email"] == email:
            return False

    # Create new user
    new_user = {
        "username": username,
        "email": email,
        "password": hash_password(password)
    }

    users.append(new_user)

    # Save users
    with open(FILE, "w") as file:
        json.dump(users, file, indent=4)

    return True


# Verify login
def verify_user(email, password):

    users = get_users()
    password = hash_password(password)

    for user in users:

        if user["email"] == email and user["password"] == password:
            return user["username"]

    return None
