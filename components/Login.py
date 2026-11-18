
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
        ).pack(pady=20)

        tk.Label(self, text="Email").pack()
        self.email = tk.Entry(self, width=30)
        self.email.pack(pady=5)

        tk.Label(self, text="Password").pack()
        self.password = tk.Entry(self, width=30, show="*")
        self.password.pack(pady=5)

        tk.Button(
            self,
            text="Login",
            command=self.login
        ).pack(pady=15)

        tk.Label(
            self,
            text="Don't have an account?"
        ).pack()

        tk.Button(
            self,
            text="Register",
            command=self.root.show_register
        ).pack(pady=5)

    # Login function
    def login(self):

        email = self.email.get().strip()
        password = self.password.get()

        if not email or not password:
            messagebox.showerror("Error", "Fill all fields")
            return

        # Check user details
        username = verify_user(email, password)

        if username:

            messagebox.showinfo("Success", "Login successful!")

            self.root.show_dashboard(username)

        else:

            messagebox.showerror(
                "Error",
                "Invalid email or password"
            )
