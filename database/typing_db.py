
import json
from pathlib import Path
from datetime import datetime

# File location
FILE = Path(__file__).resolve().parent.parent / "typing_results.json"


# Create file if missing
if not FILE.exists():
    FILE.write_text("[]")


# Read all results
def get_results():

    with open(FILE, "r") as file:
        return json.load(file)


# Save a typing result
def save_result(username, wpm, accuracy, correct, incorrect, duration):

    results = get_results()

    # Get current date and time
    now = datetime.now()

    # Create result
    new_result = {
        "username": username,
        "wpm": wpm,
        "accuracy": accuracy,
        "correct_chars": correct,
        "incorrect_chars": incorrect,
        "duration_seconds": duration,
        "date": now.strftime("%Y-%m-%d"),
        "time": now.strftime("%H:%M:%S")
    }

    # Add result to list
    results.append(new_result)

    # Save to JSON
    with open(FILE, "w") as file:
        json.dump(results, file, indent=4)


# Get results of one user
def get_user_results(username):

    results = get_results()

    user_results = []

    for result in results:

        if result["username"] == username:
            user_results.append(result)

    return user_results
