
from tkinter import *
from database import *

conn, cursor = initialize_connection()


def center_window(width, height):
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry(f'{width}x{height}+{x}+{y}')


class WelcomeWindow(Frame):
    def __init__(self, master):
        super().__init__()
        self.master = master
        self.master.title("Welcome")
        center_window(240, 120)

        login_button = Button(self, text="Login", width=10,command=self.open_login_window)
        login_button.pack(padx=20, pady=(20, 10))

        register_button = Button(self, text="Register", width=10,command=self.open_register_window)
        register_button.pack(pady=10)
        self.pack()

    def open_login_window(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.destroy()
        LoginWindow(self.master)

    def open_register_window(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.destroy()
        RegisterWindow(self.master)


class LoginWindow(Frame):
    def __init__(self, master):
        super().__init__()
        self.master = master
        self.master.title("Login")
        self.master.resizable(False, False)
        center_window(240, 150)

        Label(self, text="Username:").grid(row=0, column=0)
        self.username_entry = Entry(self)
        self.username_entry.grid(row=0, column=1, padx=10, pady=10)

        Label(self, text="Password:").grid(row=1, column=0)
        self.password_entry = Entry(self, show="*")
        self.password_entry.grid(row=1, column=1, padx=10, pady=10)

        submit_button = Button(self, text="Submit", width=8, command=self.submit)
        submit_button.grid(row=2, column=1, sticky="e", padx=10, pady=(10, 0))

        submit_button = Button(self, text="Back", width=8, command=self.back)
        submit_button.grid(row=2, column=0, sticky="w", padx=10, pady=(10, 0))
        self.pack()

    def submit(self):
        data = {}
        data["email"] = self.username_entry.get()
        data["password"] = self.password_entry.get()

        if login(cursor, data) == True:
            print("successful login")
            for widget in self.winfo_children():
                widget.destroy()
            self.destroy()
            MainWindow(self.master)
        else:
            print("unsuccessful login")

    def back(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.destroy()
        WelcomeWindow(self.master)


class RegisterWindow(Frame):
    def __init__(self, master):
        super().__init__()
        self.master = master
        self.master.title("Register")
        self.master.resizable(False, False)
        center_window(320, 350)

        Label(self, text="First Name:").grid(row=0, column=0, sticky="w")
        self.first_name_entry = Entry(self, width=26)
        self.first_name_entry.grid(row=0, column=1, padx=10, pady=10, sticky="e")

        Label(self, text="Last Name:").grid(row=1, column=0, sticky="w")
        self.last_name_entry = Entry(self, width=26)
        self.last_name_entry.grid(row=1, column=1, padx=10, pady=10, sticky="e")

        Label(self, text="Password:").grid(row=2, column=0, sticky="w")
        self.password_entry = Entry(self, show="*", width=26)
        self.password_entry.grid(row=2, column=1, padx=10, pady=10, sticky="e")

        Label(self, text="Email:").grid(row=3, column=0, sticky="w")
        self.email_entry = Entry(self, width=26)
        self.email_entry.grid(row=3, column=1, padx=10, pady=10, sticky="e")

        Label(self, text="Gender:").grid(row=4, column=0, sticky="w")
        self.gender_entry = Entry(self, width=10)
        self.gender_entry.grid(row=4, column=1, padx=10, pady=10, sticky="e")

        Label(self, text="Age:").grid(row=5, column=0, sticky="w")
        self.age_entry = Entry(self, width=10)
        self.age_entry.grid(row=5, column=1, padx=10, pady=10, sticky="e")

        Label(self, text="Address:").grid(row=6, column=0, sticky="w")
        self.address_entry = Text(self, width=20, height=3)
        self.address_entry.grid(row=6, column=1, padx=10, pady=10, sticky="e")

        submit_button = Button(self, text="Submit", width=8, command=self.submit)
        submit_button.grid(row=7, column=1, padx=10, pady=10, sticky="e")

        submit_button = Button(self, text="Back", width=8, command=self.back)
        submit_button.grid(row=7, column=0, sticky="w", padx=10, pady=(10, 10))
        self.pack()

    def submit(self):
        data = {}
        data["firstName"] = self.first_name_entry.get()
        data["lastName"] = self.last_name_entry.get()
        data["password"] = self.password_entry.get()
        data["email"] = self.email_entry.get()
        data["gender"] = self.gender_entry.get()
        data["age"] = self.age_entry.get()
        data["address"] = self.address_entry.get(1.0, END)

        register(cursor, conn, data)

    def back(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.destroy()
        WelcomeWindow(self.master)

class MainWindow(Frame):
    def __init__(self, master):
        super().__init__()
        self.master = master
        center_window(600, 400)
        self.pack()

root = Tk()
WelcomeWindow(root)
root.mainloop()
