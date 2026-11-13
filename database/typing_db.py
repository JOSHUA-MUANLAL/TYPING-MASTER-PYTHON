
import json
from pathlib import Path
from datetime import datetime

FILE = Path(__file__).resolve().parent.parent / "typing_results.json"


# Create file if missing
def initialize_file():

    if not FILE.exists():
        FILE.write_text("[]", encoding="utf-8")


# Read all results safely
def get_results():

    initialize_file()

    try:
        with open(FILE, "r", encoding="utf-8") as f:
            data = json.load(f)

            if isinstance(data, list):
                return data

            return []

    except (json.JSONDecodeError, OSError):
        return []


# Save typing result
def save_result(username, wpm, accuracy, correct, incorrect, duration):

    results = get_results()

    new_result = {
        "username": username,
        "wpm": wpm,
        "accuracy": accuracy,
        "correct_chars": correct,
        "incorrect_chars": incorrect,
        "duration_seconds": duration,
        "date": datetime.now().strftime("%Y-%m-%d"),
        "time": datetime.now().strftime("%H:%M:%S")
    }

    results.append(new_result)

    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=4)


# Get results of a particular user
def get_user_results(username):

    results = get_results()

    return [
        result for result in results
        if result["username"] == username
    ]
