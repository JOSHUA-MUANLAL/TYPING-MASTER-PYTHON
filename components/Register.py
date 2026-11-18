
import tkinter as tk
from tkinter import messagebox
import re

from database.db import create_user


class Register(tk.Frame):

    def __init__(self, root):
        super().__init__(root)

        self.root = root

        tk.Label(
            self,
            text="Create Account",
            font=("Arial", 24, "bold")
        ).pack(pady=20)

        # Username
        tk.Label(self, text="Username").pack()
        self.username = tk.Entry(self, width=30)
        self.username.pack(pady=5)

        # Email
        tk.Label(self, text="Email").pack()
        self.email = tk.Entry(self, width=30)
        self.email.pack(pady=5)

        # Password
        tk.Label(self, text="Password").pack()
        self.password = tk.Entry(self, width=30, show="*")
        self.password.pack(pady=5)

        # Register button
        tk.Button(
            self,
            text="Register",
            command=self.register
        ).pack(pady=15)

        # Back button
        tk.Button(
            self,
            text="Back to Login",
            command=self.root.show_login
        ).pack()

    # Registration function
    def register(self):

        username = self.username.get().strip()
        email = self.email.get().strip()
        password = self.password.get()

        # Check empty fields
        if not username or not email or not password:
            messagebox.showerror("Error", "Fill all fields")
            return

        
        # Check email using regex
        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

        if not re.match(pattern, email):
            messagebox.showerror("Error", "Invalid email")
            return

        # Check password length
        if len(password) < 6:
            messagebox.showerror(
                "Error",
                "Password must be at least 6 characters"
            )
            return

        # Save user
        success = create_user(username, email, password)

        if success:
            messagebox.showinfo("Success", "Account created!")
            self.root.show_login()

        else:
            messagebox.showerror("Error", "Email already exists")
