
import tkinter as tk
from tkinter import messagebox

from database.db import create_user


class Register(tk.Frame):

    def __init__(self, root):
        super().__init__(root)

        self.root = root

        tk.Label(
            self,
            text="Create Account",
            font=("Arial", 25, "bold")
        ).pack(pady=25)

        tk.Label(self, text="Username").pack()

        self.username = tk.Entry(self, width=35)
        self.username.pack(pady=5)

        tk.Label(self, text="Email").pack()

        self.email = tk.Entry(self, width=35)
        self.email.pack(pady=5)

        tk.Label(self, text="Password").pack()

        self.password = tk.Entry(
            self,
            width=35,
            show="*"
        )
        self.password.pack(pady=5)

        tk.Button(
            self,
            text="Create Account",
            width=20,
            command=self.register
        ).pack(pady=20)

        tk.Button(
            self,
            text="Back to Login",
            command=self.root.show_login
        ).pack()

    def register(self):

        username = self.username.get().strip()
        email = self.email.get().strip()
        password = self.password.get()

        if not username or not email or not password:

            messagebox.showerror(
                "Error",
                "All fields are required"
            )
            return

        if "@" not in email or "." not in email:

            messagebox.showerror(
                "Error",
                "Enter a valid email"
            )
            return

        if len(password) < 6:

            messagebox.showerror(
                "Error",
                "Password must contain at least 6 characters"
            )
            return

        success = create_user(
            username,
            email,
            password
        )

        if success:

            messagebox.showinfo(
                "Success",
                "Account created successfully!"
            )

            self.root.show_login()

        else:

            messagebox.showerror(
                "Error",
                "Email already registered!"
            )
