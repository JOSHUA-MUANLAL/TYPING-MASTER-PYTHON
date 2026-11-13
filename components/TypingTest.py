
import tkinter as tk
from tkinter import messagebox
import random
import time

from database.typing_db import save_result


class TypingTest(tk.Frame):

    def __init__(self, root, duration, username):
        super().__init__(root)

        self.root = root
        self.duration = duration
        self.username = username

        self.remaining = duration
        self.start_time = None
        self.timer_id = None
        self.finished = False

        # Random paragraphs
        self.paragraphs = [

            "Technology has changed the way people communicate "
            "and share information. Today we can connect with "
            "anyone around the world within seconds.",

            "Learning a new skill requires patience and consistency. "
            "Small improvements every day can lead to great "
            "achievements.",

            "Programming is the art of solving problems using "
            "logical thinking. A good programmer always tries "
            "to write clean and efficient code.",

            "The internet has made education accessible to "
            "millions of people. Students can now learn new "
            "subjects from anywhere in the world.",

            "Success does not come overnight. It requires "
            "dedication, discipline, hard work and the "
            "willingness to learn from mistakes.",

            "Python is a popular programming language used "
            "in web development, automation, artificial "
            "intelligence and data science."
        ]

        self.target_text = random.choice(self.paragraphs)

        # Heading
        tk.Label(
            self,
            text="Typing Speed Test",
            font=("Arial", 24, "bold")
        ).pack(pady=15)

        # Duration
        tk.Label(
            self,
            text=f"Test Duration: {duration} Seconds",
            font=("Arial", 12)
        ).pack()

        # Timer
        self.timer_label = tk.Label(
            self,
            text=f"Time: {self.remaining}s",
            font=("Arial", 20, "bold"),
            fg="red"
        )
        self.timer_label.pack(pady=15)

        # Target paragraph
        tk.Label(
            self,
            text="Type the following paragraph:",
            font=("Arial", 12, "bold")
        ).pack(pady=10)

        self.paragraph_label = tk.Label(
            self,
            text=self.target_text,
            font=("Arial", 13),
            wraplength=580,
            justify="left",
            bg="#eeeeee",
            padx=15,
            pady=15
        )
        self.paragraph_label.pack(
            padx=25,
            pady=10,
            fill="x"
        )

        # Typing area
        self.text_area = tk.Text(
            self,
            height=7,
            width=65,
            font=("Arial", 13),
            wrap="word"
        )
        self.text_area.pack(
            padx=25,
            pady=15
        )

        self.text_area.focus_set()

        # Statistics
        self.stats_label = tk.Label(
            self,
            text="WPM: 0    Accuracy: 100%",
            font=("Arial", 13, "bold")
        )
        self.stats_label.pack(pady=10)

        self.char_label = tk.Label(
            self,
            text="Correct: 0    Incorrect: 0",
            font=("Arial", 11)
        )
        self.char_label.pack()

        # Detect typing
        self.text_area.bind(
            "<KeyRelease>",
            self.check_typing
        )

        # Back button
        tk.Button(
            self,
            text="Back to Dashboard",
            command=self.go_back
        ).pack(pady=15)

    # Check typing
    def check_typing(self, event=None):

        if self.finished:
            return

        typed_text = self.text_area.get(
            "1.0",
            "end-1c"
        )

        # Start timer on first character
        if self.start_time is None and typed_text:

            self.start_time = time.monotonic()

            self.update_timer()

        self.calculate_stats()

    # Timer
    def update_timer(self):

        if self.finished:
            return

        elapsed = time.monotonic() - self.start_time

        self.remaining = max(
            0,
            self.duration - int(elapsed)
        )

        self.timer_label.config(
            text=f"Time: {self.remaining}s"
        )

        if elapsed >= self.duration:

            self.finish_test()

        else:

            self.timer_id = self.after(
                100,
                self.update_timer
            )

    # Calculate WPM and accuracy
    def calculate_stats(self):

        typed_text = self.text_area.get(
            "1.0",
            "end-1c"
        )

        correct = 0
        incorrect = 0

        for i, char in enumerate(typed_text):

            if (
                i < len(self.target_text)
                and char == self.target_text[i]
            ):
                correct += 1

            else:
                incorrect += 1

        total = len(typed_text)

        accuracy = (
            (correct / total) * 100
            if total > 0 else 100
        )

        if self.start_time is not None:

            elapsed = max(
                time.monotonic() - self.start_time,
                0.001
            )

        else:

            elapsed = 0.001

        wpm = (correct / 5) / (elapsed / 60)

        self.stats_label.config(
            text=f"WPM: {int(wpm)}    Accuracy: {accuracy:.1f}%"
        )

        self.char_label.config(
            text=f"Correct: {correct}    Incorrect: {incorrect}"
        )

        return {
            "wpm": round(wpm, 2),
            "accuracy": round(accuracy, 2),
            "correct": correct,
            "incorrect": incorrect
        }

    # Finish test
    def finish_test(self):

        if self.finished:
            return

        self.finished = True

        if self.timer_id:

            self.after_cancel(self.timer_id)
            self.timer_id = None

        self.text_area.config(state="disabled")

        # Calculate final result
        stats = self.calculate_stats()

        # Save to JSON
        save_result(
            username=self.username,
            wpm=stats["wpm"],
            accuracy=stats["accuracy"],
            correct=stats["correct"],
            incorrect=stats["incorrect"],
            duration=self.duration
        )

        # Display result
        messagebox.showinfo(
            "Test Completed",

            f"Your typing test is complete!\n\n"
            f"WPM: {stats['wpm']}\n"
            f"Accuracy: {stats['accuracy']}%\n"
            f"Correct Characters: {stats['correct']}\n"
            f"Incorrect Characters: {stats['incorrect']}\n\n"
            f"Result saved successfully!"
        )

    # Return to dashboard
    def go_back(self):

        if self.timer_id:

            self.after_cancel(self.timer_id)
            self.timer_id = None

        self.root.show_dashboard(self.username)
