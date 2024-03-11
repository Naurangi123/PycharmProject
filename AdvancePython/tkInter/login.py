import mysql.connector
from tkinter import *
from tkinter import messagebox
import sys





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


class RegisterWindow:
    def __init__(self, parent, root):
        self.parent = parent
        self.root = root
        self.parent.title("Registration Form")
        self.font1 = ('arial', 14, "bold")

        self.F2 = LabelFrame(self.parent, text="Registration Form", bg="lightgreen", font=('arial', 14, 'bold'))
        self.F2.pack(padx=10, pady=10, side="top", anchor="center")

        label_first_name = Label(self.F2, text="First Name:", font=self.font1)
        label_first_name.grid(row=0, column=0, padx=10, pady=5, sticky="E")
        self.e1 = Entry(self.F2)
        self.e1.grid(row=0, column=1, padx=10, pady=5)

        label_last_name = Label(self.F2, text="Last Name:", font=self.font1)
        label_last_name.grid(row=1, column=0, padx=10, pady=5, sticky="E")
        self.e2 = Entry(self.F2)
        self.e2.grid(row=1, column=1, padx=10, pady=5)

        label_email = Label(self.F2, text="Email:", font=self.font1)
        label_email.grid(row=2, column=0, padx=10, pady=5, sticky="E")
        self.e3 = Entry(self.F2)
        self.e3.grid(row=2, column=1, padx=10, pady=5)

        label_password = Label(self.F2, text="Password:", font=self.font1)
        label_password.grid(row=3, column=0, padx=10, pady=5, sticky="E")
        self.e4 = Entry(self.F2, show="*")
        self.e4.grid(row=3, column=1, padx=10, pady=5)

        submit_button = Button(self.F2, text="Submit", font=self.font1, command=self.submit_registration)
        submit_button.grid(row=4, column=1, pady=10)

        back_btn = Button(self.F2, text="Back", font=self.font1, command=self.back)
        back_btn.grid(row=4, column=0, padx=10, pady=5)

    def submit_registration(self):
        first_name = self.e1.get()
        last_name = self.e2.get()
        email = self.e3.get()
        password = self.e4.get()

        # Check if the email already exists in the database
        cursor.execute("SELECT * FROM Users WHERE email=%s", (email,))
        existing_user = cursor.fetchone()

        if existing_user:
            messagebox.showerror("Error", "Email already registered. Please use a different email.")
        else:
            # Insert the user into the database
            cursor.execute("INSERT INTO Users (first_name, last_name, email, password) VALUES (%s, %s, %s, %s)",
                           (first_name, last_name, email, password))
            conn.commit()
            messagebox.showinfo("Success", "Registration successful.")
            self.parent.destroy()  # Close the registration window after successful registration
            self.open_medicine_window()  # Bring back the main window
    def back(self):
        self.parent.destroy()
        self.root.deiconify()


    def open_medicine_window(self):
        from medicine import Bill_App
        self.parent.destroy()
        bill_window=Toplevel(self.root)
        Bill_App(bill_window)


class LoginWindow:
    def __init__(self, parent, root):
        self.parent = parent
        self.root = root
        self.parent.title("Login Form")
        self.font1 = ('arial', 14, "bold")

        self.F3 = LabelFrame(self.parent, text="Login Form", bg="lightgreen", font=('arial', 14, 'bold'))
        self.F3.pack(padx=10, pady=10, side="top", anchor="center")

        label_username = Label(self.F3, text="Email:", font=self.font1)
        label_username.grid(row=0, column=0, padx=10, pady=5, sticky="E")
        self.e1 = Entry(self.F3, width=10)
        self.e1.grid(row=0, column=1, padx=10, pady=5)

        label_password = Label(self.F3, text="Password:", font=self.font1)
        label_password.grid(row=1, column=0, padx=10, pady=5, sticky="E")
        self.e2 = Entry(self.F3, width=10, show="*")
        self.e2.grid(row=1, column=1, padx=10, pady=5)

        login_button = Button(self.F3, text="Login", font=self.font1, command=self.submit_login)
        login_button.grid(row=2, column=1, pady=10)

        back_btn=Button(self.F3,text="Back",font=self.font1,command=self.back)
        back_btn.grid(row=2,column=0,padx=10,pady=5)

    def submit_login(self):
        email = self.e1.get()
        password = self.e2.get()

        cursor.execute("SELECT * FROM Users WHERE email=%s AND password=%s", (email, password))
        user = cursor.fetchone()

        if user:
            messagebox.showinfo("Success", "Login successful.") # Close the login window after successful login
            self.parent.destroy()
            self.root.deiconify()
            self.open_medicine_window()
        else:
            messagebox.showerror("Error", "Invalid email or password.")



    def back(self):
        self.parent.destroy()
        self.root.deiconify()

    def open_medicine_window(self):
        from medicine import Bill_App
        self.parent.destroy()
        bill_window=Toplevel(self.root)
        Bill_App(bill_window)



class MainApplication:
    def __init__(self, root):
        self.root = root
        self.root.title("Main Application")
        self.font1 = ('arial', 14, "bold")

        F1 = LabelFrame(self.root, text="Main Form", bg="lightgreen", font=('arial', 14, 'bold'))
        F1.pack(padx=10, pady=10, side="top", anchor="center")

        register_button = Button(F1, text="Register", font=self.font1, command=self.open_register_window)
        register_button.grid(row=4, column=0, pady=10)

        login_button = Button(F1, text="Login", font=self.font1, command=self.open_login_window)
        login_button.grid(row=4, column=1, pady=10)

    def open_register_window(self):
        self.root.withdraw()  # Hide the main window
        register_window = Toplevel(self.root)
        RegisterWindow(register_window,self.root)

    def open_login_window(self):
        self.root.withdraw()  # Hide the main window
        login_window = Toplevel(self.root)
        LoginWindow(login_window,self.root)

    def open_medicine_window(self):
        from medicine import Bill_App
        self.parent.deiconify()
        bill_window=Toplevel(self.root)
        Bill_App(bill_window)

    def exit(self):
        self.root.destroy()
        sys.exit()



root = Tk()
obj=MainApplication(root)
root.mainloop()

