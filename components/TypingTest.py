
import tkinter as tk
from tkinter import messagebox
import random
import time

from database.typing_db import save_result


class TypingTest(tk.Frame):

    def __init__(self, root, username, duration):
        super().__init__(root)

        self.root = root
        self.username = username
        self.duration = duration
        self.remaining = duration
        self.started = False
        self.finished = False

        # Paragraph list
        self.paragraphs = [

            "The National Institute of Technology Meghalaya is one of the "
            "National Institutes of Technology in India. Located in the "
            "beautiful hills of Sohra, the institute provides quality education "
            "in engineering, science, and technology. Students are encouraged "
            "to participate in research, innovation, technical events, and "
            "various extracurricular activities. The peaceful environment "
            "provides an excellent atmosphere for learning and personal growth.",

            "Programming is not just about writing lines of code. It is about "
            "understanding problems, developing logical thinking, and finding "
            "efficient solutions. A good programmer spends time understanding "
            "the requirements before starting to write a program. Learning "
            "different programming languages, practising data structures, "
            "and building real-world projects can help students become "
            "confident and skilled software developers.",

            "Technology has become an important part of our everyday lives. "
            "From smartphones and computers to artificial intelligence and "
            "cloud computing, modern technology continues to change the way "
            "people communicate, learn, and work. Businesses use technology "
            "to improve productivity, while students use digital platforms "
            "to access educational resources. However, responsible use of "
            "technology is equally important for a better digital future.",

            "Success does not happen overnight. It requires patience, "
            "discipline, consistency, and the willingness to learn from "
            "mistakes. Sometimes progress may seem slow, but every small "
            "improvement brings us closer to our goals. Instead of comparing "
            "ourselves with others, we should focus on becoming better than "
            "we were yesterday. Hard work combined with determination "
            "can turn difficult challenges into valuable opportunities.",

            "The internet has transformed the way information is shared "
            "across the world. People can communicate instantly, attend "
            "online classes, work remotely, and access information within "
            "seconds. Developers create websites and applications that "
            "connect millions of users every day. Despite these advantages, "
            "users should remain careful about online privacy, cybersecurity, "
            "misinformation, and the safe handling of personal information.",

            "A computer system consists of hardware and software working "
            "together to perform different tasks. The operating system "
            "manages memory, processes, files, and input-output devices. "
            "It provides an interface between the user and the computer "
            "hardware. Understanding operating system concepts such as "
            "process scheduling, memory management, deadlocks, and file "
            "systems is essential for every computer science student."
        ]

        self.target_text = random.choice(self.paragraphs)

        # Heading
        tk.Label(
            self,
            text="Typing Speed Test",
            font=("Arial", 24, "bold")
        ).pack(pady=15)

        # Timer
        self.timer_label = tk.Label(
            self,
            text=f"Time: {duration}",
            font=("Arial", 20),
            fg="red"
        )
        self.timer_label.pack()

        # Paragraph
        tk.Label(
            self,
            text=self.target_text,
            wraplength=600,
            font=("Arial", 14)
        ).pack(pady=20)

        # Typing area
        self.text_area = tk.Text(self, height=6, width=60)
        self.text_area.pack(pady=10)
        self.text_area.focus_set()

        # Statistics
        self.stats_label = tk.Label(
            self,
            text="WPM: 0    Accuracy: 100%"
        )
        self.stats_label.pack(pady=10)

        # Detect typing
        self.text_area.bind("<KeyRelease>", self.check_typing)

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

        typed = self.text_area.get("1.0", "end-1c")

        # Start timer on first character
        if not self.started and typed:
            self.started = True
            self.start_time = time.time()
            self.update_timer()

        self.calculate_stats()

    # Countdown timer
    def update_timer(self):

        if self.finished:
            return

        self.remaining -= 1
        self.timer_label.config(text=f"Time: {self.remaining}")

        if self.remaining <= 0:
            self.finish_test()
        else:
            self.after(1000, self.update_timer)

    # Calculate statistics
    def calculate_stats(self):

        typed = self.text_area.get("1.0", "end-1c")

        correct = 0

        for i in range(len(typed)):
            if i < len(self.target_text) and typed[i] == self.target_text[i]:
                correct += 1

        total = len(typed)
        incorrect = total - correct

        # Accuracy
        accuracy = (correct / total) * 100 if total > 0 else 100

        # WPM
        if self.started:
            elapsed = time.time() - self.start_time
            wpm = (correct / 5) / (elapsed / 60) if elapsed > 0 else 0
        else:
            wpm = 0

        self.stats_label.config(
            text=f"WPM: {int(wpm)}    Accuracy: {accuracy:.1f}%"
        )

        return wpm, accuracy, correct, incorrect

    # Finish test
    def finish_test(self):

        if self.finished:
            return

        self.finished = True

        self.text_area.config(state="disabled")

        wpm, accuracy, correct, incorrect = self.calculate_stats()

        # Save result
        save_result(
            self.username,
            round(wpm, 2),
            round(accuracy, 2),
            correct,
            incorrect,
            self.duration
        )

        messagebox.showinfo(
            "Test Completed",
            f"WPM: {int(wpm)}\n"
            f"Accuracy: {accuracy:.1f}%\n"
            f"Correct: {correct}\n"
            f"Incorrect: {incorrect}"
        )

    # Back to dashboard
    def go_back(self):
        self.finished = True
        self.root.show_dashboard(self.username)
