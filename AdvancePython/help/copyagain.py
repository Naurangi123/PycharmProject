import datetime
from tkinter import *
import random
from tkinter import messagebox

class Bill_App:
    def __init__(self, root):
        self.exit_app = None
        self.clear_data = None
        self.total = None
        self.root = root
        self.root.geometry("1450x700+0+0")
        self.root.title("Bill-Dashboard")
        bg_color = "lightgreen"
        title = Label(self.root, text="Bill-Dashboard", font=('times new roman', 30, 'bold'), pady=2, bd=12, bg="lightgreen", fg="Black", relief=GROOVE)
        title.pack(fill=X)

        # Variables
        self.p_name = StringVar()
        self.p_phone = StringVar()
        self.p_dob = StringVar()
        self.p_add = StringVar()
        self.p_sx = StringVar()
        self.p_bill_no = StringVar()
        x = random.randint(500, 999)
        self.p_bill_no.set(str(x))
        self.curr_date = StringVar()

        # Customer Details
        F1 = LabelFrame(self.root, text="Customer Details", font=('times new roman', 15, 'bold'), bd=7, fg="Black", bg="lightgreen")
        F1.place(x=0, y=75, width=1280, height=130)

        labels = ["Patient Name", "Address", "DoB", "Mobile", "Sex", "Bill No.", "Current Date"]
        entries = [self.p_name, self.p_add, self.p_dob, self.p_phone, self.p_sx, self.p_bill_no, self.curr_date]

        for i in range(len(labels)):
            label = Label(F1, text=labels[i], bg="lightgreen", font=('times new roman', 15, 'bold'))
            label.grid(row=0, column=i * 2, padx=20, pady=5)

            entry = Entry(F1, width=15, textvariable=entries[i], font='arial 15', bd=7, relief=GROOVE)
            entry.grid(row=0, column=i * 2 + 1, pady=5, padx=10)

        # Medical Details
        F2 = LabelFrame(self.root, text="Medicine Name", font=('times new roman', 16, 'bold'), bd=10, fg="Black", bg="lightgreen")
        F2.place(x=0, y=205, width=940, height=300)

        medicine_labels = ["Sanitizer", "Hand Gloves", "Dettol", "Newsprin", "Thermal Gun"]
        self.med_vars = [StringVar() for _ in range(len(medicine_labels))]

        for i in range(len(medicine_labels)):
            lbl = Label(F2, text=medicine_labels[i], font=('times new roman', 14, 'bold'), bg="lightgreen", fg="black")
            lbl.grid(row=i, column=0, padx=5, pady=0, sticky='W')

            txt = Entry(F2, width=10, textvariable=self.med_vars[i], font=('times new roman', 14, 'bold'), bd=5, relief=GROOVE)
            txt.grid(row=i, column=1, padx=2, pady=5)

        # Bill Area
        F5 = Frame(self.root, bd=10, relief=GROOVE)
        F5.place(x=945, y=205, width=330, height=300)

        bill_title = Label(F5, text="Bill Area", font='arial 15 bold', bd=7, relief=GROOVE)
        bill_title.pack(fill=X)

        scroll_y = Scrollbar(F5, orient=VERTICAL)
        self.txtarea = Text(F5, yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH, expand=1)

        # Button Frame
        F6 = LabelFrame(self.root, text="Bill Area", font=('times new roman', 14, 'bold'), bd=10, fg="Black", bg="lightgreen")
        F6.place(x=0, y=505, width=650, height=145)

        # Buttons
        F4 = LabelFrame(self.root, text="Generate All", font=('times new roman', 14, 'bold'), bd=10, fg="Black", bg="lightgreen")
        F4.place(x=650, y=505, width=620, height=145)

        buttons = [("Total", self.total), ("Generate Bill", self.bill_area), ("Clear", self.clear_data), ("Exit", self.exit_app)]

        for i, (text, command) in enumerate(buttons):
            btn = Button(F4, text=text, command=command, bg="lightgreen", bd=1, fg="chocolate", pady=5, width=10, font='arial 13 bold')
            btn.grid(row=0, column=i, padx=20, pady=30)

        self.welcome_bill()

    def welcome_bill(self):
        self.txtarea.delete('1.0', END)
        self.txtarea.insert(END, "\tWelcome Medical Store ")
        self.txtarea.insert(END, f"\nPatient name: {self.p_name.get()}")
        self.txtarea.insert(END, f"\nAddress: {self.p_add.get()}")
        self.txtarea.insert(END, f"\nDoB: {self.p_dob.get()}")
        self.txtarea.insert(END, f"\nMobile No.: {self.p_phone.get()}")
        self.txtarea.insert(END, f"\nSex: {self.p_sx.get()}")
        self.txtarea.insert(END, f"\nBill No.: {self.p_bill_no.get()}")
        self.txtarea.insert(END, f"\nCurrent Date: {self.curr_date.get()}")
        self.txtarea.insert(END, f"\n================================")
        self.txtarea.insert(END, f"\nProducts\t\tQTY\t\tPrice")

    def bill_area(self, medicine_labels=None):
        if self.p_name.get() == "" or self.p_phone.get() == "":
            messagebox.showerror("Error", "Customer Details Are Must")
            return

        self.welcome_bill()

        # Medical
        for i in range(len(self.med_vars)):
            if self.med_vars[i].get() != 0:
                self.txtarea.insert(END, f"\n {medicine_labels[i]}\t\t{self.med_vars[i].get()}\t\t{self.get_med_price(i)}")

        self.txtarea.insert(END, f"\n Total Bil:\t\t\t Rs.{self.total_bill}")
        self.txtarea.insert(END, f"\n--------------------------------")
        self.save_bill()

    def get_med_price(self, index):
        # Define your prices for each medicine
        pass


root = Tk()
obj = Bill_App(root)
root.mainloop()
