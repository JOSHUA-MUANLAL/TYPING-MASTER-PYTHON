
import tkinter as tk

from components.Login import Login
from components.Register import Register
from components.Dashboard import Dashboard
from components.TypingTest import TypingTest


class App(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title("Typing Master")
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        self.geometry(f"{screen_width}x{screen_height}")
        self.resizable(False, False)

        self.show_login()

    # Clear current page
    def clear(self):

        for widget in self.winfo_children():
            widget.destroy()

    # Login
    def show_login(self):

        self.clear()
        Login(self).pack(fill="both", expand=True)

    # Register
    def show_register(self):

        self.clear()
        Register(self).pack(fill="both", expand=True)

    # Dashboard
    def show_dashboard(self, username):

        self.clear()
        Dashboard(self, username).pack(fill="both", expand=True)

    # Typing test
    def show_typing_test(self, duration, username):

        self.clear()

        TypingTest(
            self,
            duration,
            username
        ).pack(fill="both", expand=True)


if __name__ == "__main__":

    app = App()
    app.mainloop()
