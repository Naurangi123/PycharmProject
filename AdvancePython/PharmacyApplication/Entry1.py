from tkinter import *

class EntryForm:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1450x700+0+0")
        self.root.title("Entry Form")

        self.total_payable = StringVar()

        # ======================MEDICINE VARIABLES===================
        self.medi_names = [StringVar() for _ in range(14)]

        # ======================QTY VARIABLES=========================
        self.qty = [IntVar() for _ in range(14)]

        # ======================PRICE VARIABLES=======================
        self.price = [IntVar() for _ in range(14)]

        # ======================GST VARIABLES=========================
        self.gst = [StringVar() for _ in range(14)]

        # ======================SGST VARIABLES========================
        self.sgst = [StringVar() for _ in range(14)]

        # ======================CGST VARIABLES========================
        self.cgst = [StringVar() for _ in range(14)]

        # ======================AMOUNT VARIABLES=======================
        self.amount = [StringVar() for _ in range(14)]

        # ======================QTY*PRICE VARIABLES=======================
        self.total_var = [IntVar() for _ in range(14)]

        # ======================================== FRAME ==================================
        F1 = LabelFrame(self.root, text="Buyer Details", bg="orange", relief=GROOVE)
        F1.place(x=0, y=5, width=840, height=640)

        # Function to create entry widgets for each field
        def create_entries(label_text, row, col, textvars):
            Label(F1, text=label_text, bg="orange").grid(row=0, column=col, padx=20, pady=10)
            for i, var in enumerate(textvars, start=1):
                Entry(F1, width=15, textvariable=var).grid(row=i, column=col, padx=10, pady=10)

        create_entries("Medicine Name:", 0, 0, self.medi_names)
        create_entries("Quality", 1, 1, self.qty)
        create_entries("Price", 2, 2, self.price)
        create_entries("GST", 3, 3, self.gst)
        create_entries("CGST", 4, 4, self.cgst)
        create_entries("SGST", 5, 5, self.sgst)
        create_entries("Amount:", 6, 6, self.amount)

        F2 = Label(self.root, font='arial 15 bold', bd=5, relief=GROOVE)
        F2.place(x=845, y=10, width=430, height=575)

        scroll_y = Scrollbar(F2, orient=VERTICAL)
        self.txtarea = Text(F2, yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH, expand=1)
        self.welcome_bill()

        F3 = Label(self.root, font='arial 15 bold', bg="orange", bd=5, relief=GROOVE)
        F3.place(x=875, y=590, width=400, height=50)
        sbmt_btn = Button(F3, command=self.submit, text="Submit", width=6, padx=5, pady=5)
        sbmt_btn.grid(row=0, column=0, padx=180, pady=2)

    def welcome_bill(self):
        self.txtarea.delete("3.0", END)
        self.txtarea.insert(END, "\n\t\t Medicine details")
        self.txtarea.insert(END, "\nmedicine\t\tQty\t\tPrice\t  Amount")
        self.submit()

    def submit(self):
        entries = [
            (self.medi_names[i].get(), self.qty[i].get(), self.price[i].get(), self.amount[i].get())
            for i in range(14)
        ]
        for i, (name, qty, price, amount) in enumerate(entries):
            qty = qty if qty else 0
            price = price if price else 0

            # Update the entry fields with 0 if they were empty
            self.qty[i].set(qty)
            self.price[i].set(price)
            self.amount[i].set(qty * price)

            if qty == 0 and price == 0 and amount == 0:
                continue

            self.txtarea.insert(END,f"{name}\t\t{qty}\t\t{price}\t\t{amount}\n")

        self.total()

    def total(self):
        total_vars = [self.total_var[i] for i in range(14)]

        for i in range(14):
            total_result = int(self.qty[i].get()) * float(self.price[i].get())
            total_vars[i].set(total_result)

        total_payable_amount = sum(map(lambda x: x.get(), total_vars))
        self.total_payable.set(total_payable_amount)


root = Tk()
obj = EntryForm(root)
root.mainloop()
