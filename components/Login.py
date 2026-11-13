
import tkinter as tk
from tkinter import messagebox

from database.db import verify_user


class Login(tk.Frame):

    def __init__(self, root):
        super().__init__(root)

        self.root = root

        tk.Label(
            self,
            text="Typing Master",
            font=("Arial", 25, "bold")
        ).pack(pady=25)

        tk.Label(
            self,
            text="Login to your account",
            font=("Arial", 13)
        ).pack(pady=5)

        tk.Label(self, text="Email").pack(pady=5)

        self.email = tk.Entry(self, width=35)
        self.email.pack(pady=5)

        tk.Label(self, text="Password").pack(pady=5)

        self.password = tk.Entry(
            self,
            width=35,
            show="*"
        )
        self.password.pack(pady=5)

        tk.Button(
            self,
            text="Login",
            width=20,
            command=self.login
        ).pack(pady=20)

        tk.Label(
            self,
            text="Don't have an account?"
        ).pack()

        tk.Button(
            self,
            text="Register",
            command=self.root.show_register
        ).pack(pady=5)

    def login(self):

        email = self.email.get().strip()
        password = self.password.get()

        if not email or not password:

            messagebox.showerror(
                "Error",
                "All fields are required"
            )
            return

        username = verify_user(email, password)

        if username:

            messagebox.showinfo(
                "Success",
                "Login successful!"
            )

            self.root.show_dashboard(username)

        else:

            messagebox.showerror(
                "Error",
                "Invalid email or password"
            )
