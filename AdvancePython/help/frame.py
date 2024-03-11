# from tkinter import *
#
# root = Tk()
# root.title("")
# font1 = ('arial', 14, "bold")
#
# label = LabelFrame(root, text="Login", bg="green", font=font1, height=400, width=350)
# label.pack(pady=120)
#
# lf = Frame(label, text="FirstName", font=font1)
# lf.place(x=10, y=15)
# e1 = Entry(lf, width=15)
# e1.pack()
#
# ll = Frame(label, text="LastName", font=font1)
# ll.place(x=10, y=55)
# e2 = Entry(ll, width=15)
# e2.pack()
#
# eMail = Frame(label, text="Email", font=font1)
# eMail.place(x=10, y=90)
# e3 = Entry(eMail, width=15)
# e3.pack()
#
# Pass = Frame(label, text="Password", font=font1)
# Pass.place(x=10, y=130)
# e4 = Entry(Pass, width=15)
# e4.pack()
#
# root.mainloop()

from tkinter import *

root = Tk()
root.title("")
font1 = ('arial', 14, "bold")

label = LabelFrame(root, text="Login", bg="green", font=font1, height=400, width=350)
label.pack(pady=120)

lf = Frame(label, font=font1)
lf.place(x=10, y=15)
e1 = Entry(lf, width=15)
e1.pack()

ll = Frame(label,  font=font1)
ll.place(x=10, y=55)
e2 = Entry(ll, width=15)
e2.pack()

eMail = Frame(label,  font=font1)
eMail.place(x=10, y=90)
e3 = Entry(eMail, width=15)
e3.pack()

Pass = Frame(label,  font=font1)
Pass.place(x=10, y=130)
e4 = Entry(Pass, width=15)
e4.pack()

root.mainloop()
def submit():
    # Retrieve values from entry widgets
    first_name = entry_first_name.get()
    last_name = entry_last_name.get()
    email = entry_email.get()
    password = entry_password.get()

    # Print or process the retrieved values (you can customize this part)
    print("First Name:", first_name)
    print("Last Name:", last_name)
    print("Email:", email)
    print("Password:", password)
