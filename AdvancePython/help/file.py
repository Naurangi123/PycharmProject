from tkinter import *
from tkinter import messagebox

import mysql.connector

# Connect to the MySQL database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="naurangi@234",
    database="user_data"
)
cursor = conn.cursor()

# Create the Users table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        first_name VARCHAR(255),
        last_name VARCHAR(255),
        email VARCHAR(255),
        password VARCHAR(255)
    )
''')
conn.commit()


class RegisterLoginForm:
    def __init__(self, root, main_app):
        self.root = root
        self.main_app = main_app
        self.root.title("Registration/Login Form")
        self.font1 = ('arial', 14, "bold")
        self.medicine = Bill_App(self.root)

        self.label_frame = LabelFrame(self.root, text="Form", bg="lightgreen", font=self.font1)
        self.label_frame.pack(padx=10, pady=10, side="top", anchor="center")

        self.create_widgets()

    def create_widgets(self):
        Label(self.label_frame, text="Email:", font=self.font1).grid(row=0, column=0, padx=10, pady=5, sticky="E")
        self.email_entry = Entry(self.label_frame)
        self.email_entry.grid(row=0, column=1, padx=10, pady=5)

        Label(self.label_frame, text="Password:", font=self.font1).grid(row=1, column=0, padx=10, pady=5, sticky="E")
        self.password_entry = Entry(self.label_frame, show="*")
        self.password_entry.grid(row=1, column=1, padx=10, pady=5)

        submit_button = Button(self.label_frame, text="Submit", font=self.font1, command=self.submit_form)
        submit_button.grid(row=2, column=1, pady=10)

        back_btn = Button(self.label_frame, text="Back", font=self.font1, command=self.back)
        back_btn.grid(row=2, column=0, padx=10, pady=5)

    def submit_form(self):
        email = self.email_entry.get()
        password = self.password_entry.get()

        # Check email and password (you may want to add more validation)

        if email and password:
            # Perform database operations if needed
            messagebox.showinfo("Success", "Operation successful.")
            self.open_medicine_window()
        else:
            messagebox.showerror("Error", "Invalid input. Please fill in all fields.")

    def open_medicine_window(self):
        self.root.withdraw()
        self.medicine.show_bill_app()

    def back(self):
        self.root.destroy()
        self.main_app.root.deiconify()


class MainApplication:
    def __init__(self, root):
        self.root = root
        self.root.title("Main Application")
        self.font1 = ('arial', 14, "bold")

        F1 = LabelFrame(self.root, text="Main Form", bg="lightgreen", font=('arial', 14, 'bold'))
        F1.pack(padx=10, pady=10, side="top", anchor="center")

        register_button = Button(F1, text="Register/Login", font=self.font1, command=self.open_register_login_window)
        register_button.grid(row=4, column=0, pady=10)

    def open_register_login_window(self):
        self.root.withdraw()  # Hide the main window
        register_login_window = Toplevel(self.root)
        RegisterLoginForm(register_login_window, self)


root = Tk()
obj = MainApplication(root)
root.mainloop()
