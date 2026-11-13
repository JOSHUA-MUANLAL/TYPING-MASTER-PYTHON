
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
            text="Select your typing test duration",
            font=("Arial", 13)
        ).pack(pady=20)

        tk.Button(
            self,
            text="30 Seconds",
            width=25,
            height=2,
            command=lambda: self.start_test(30)
        ).pack(pady=10)

        tk.Button(
            self,
            text="60 Seconds",
            width=25,
            height=2,
            command=lambda: self.start_test(60)
        ).pack(pady=10)

        tk.Button(
            self,
            text="View Typing History",
            width=25,
            command=self.show_history
        ).pack(pady=20)

        tk.Button(
            self,
            text="Logout",
            width=15,
            command=self.logout
        ).pack(pady=10)

    def start_test(self, duration):

        self.root.show_typing_test(
            duration,
            self.username
        )

    def show_history(self):

        results = get_user_results(self.username)

        if not results:

            messagebox.showinfo(
                "History",
                "No typing tests completed yet."
            )
            return

        history = ""

        for i, result in enumerate(results, start=1):

            history += (
                f"\nTest {i}\n"
                f"WPM: {result['wpm']}\n"
                f"Accuracy: {result['accuracy']}%\n"
                f"Correct characters: {result['correct_chars']}\n"
                f"Incorrect characters: {result['incorrect_chars']}\n"
                f"Duration: {result['duration_seconds']} seconds\n"
                f"Date: {result['date']} {result['time']}\n"
                f"--------------------------\n"
            )

        messagebox.showinfo(
            "Typing History",
            history
        )

    def logout(self):

        self.root.show_login()
