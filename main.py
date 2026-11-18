
import tkinter as tk

from components.Login import Login
from components.Register import Register
from components.Dashboard import Dashboard
from components.TypingTest import TypingTest


class App(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title("Typing Master")
        self.geometry("900x650")

        self.show_login()

    # Remove the current screen
    def clear_screen(self):
        for widget in self.winfo_children():
            widget.destroy()

    # Show login page
    def show_login(self):
        self.clear_screen()
        Login(self).pack(expand=True)

    # Show registration page
    def show_register(self):
        self.clear_screen()
        Register(self).pack(expand=True)

    # Show dashboard
    def show_dashboard(self, username):
        self.clear_screen()
        Dashboard(self, username).pack(expand=True)

    # Show typing test
    def show_typing_test(self, username, duration):
        self.clear_screen()
        TypingTest(self, username, duration).pack(expand=True)


if __name__ == "__main__":

    app = App()
    app.mainloop()
