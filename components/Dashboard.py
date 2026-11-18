
import tkinter as tk
from tkinter import messagebox

from database.typing_db import get_user_results


class Dashboard(tk.Frame):

    def __init__(self, root, username):
        super().__init__(root)

        self.root = root
        self.username = username

        tk.Label(
            self,
            text="Typing Master",
            font=("Arial", 27, "bold")
        ).pack(pady=25)

        tk.Label(
            self,
            text=f"Welcome, {username}!",
            font=("Arial", 17)
        ).pack(pady=10)

        tk.Label(
            self,
            text="Choose your test duration"
        ).pack(pady=15)

        # Start 30-second test
        tk.Button(
            self,
            text="30 Seconds",
            width=25,
            command=lambda: self.start_test(30)
        ).pack(pady=10)

        # Start 60-second test
        tk.Button(
            self,
            text="60 Seconds",
            width=25,
            command=lambda: self.start_test(60)
        ).pack(pady=10)

        # View history
        tk.Button(
            self,
            text="Typing History",
            width=25,
            command=self.show_history
        ).pack(pady=15)

        # Logout
        tk.Button(
            self,
            text="Logout",
            command=self.root.show_login
        ).pack(pady=10)

    # Start typing test
    def start_test(self, duration):

        self.root.show_typing_test(
            self.username,
            duration
        )

    # Display typing history
    def show_history(self):

        results = get_user_results(self.username)

        if not results:
            messagebox.showinfo(
                "History",
                "No tests completed yet"
            )
            return

        history = ""

        for i, result in enumerate(results, start=1):

            history += (
                f"Test {i}\n"
                f"WPM: {result['wpm']}\n"
                f"Accuracy: {result['accuracy']}%\n"
                f"Correct: {result['correct_chars']}\n"
                f"Incorrect: {result['incorrect_chars']}\n"
                f"Duration: {result['duration_seconds']} seconds\n"
                f"Date: {result['date']}\n"
                f"Time: {result['time']}\n"
                "---------------------\n"
            )

        messagebox.showinfo("Typing History", history)
