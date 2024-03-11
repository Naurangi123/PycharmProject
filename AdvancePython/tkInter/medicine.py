from tkinter import *
import random
import os
from tkinter import messagebox

# ============main============================
class Bill_App:
    def __init__(self, root):
        self.search_bill = None
        self.cold_drinks_price = None
        self.grocery_price = None
        self.root = root
        self.root.geometry("1450x700+0+0")
        self.root.title("Bill-Dashboard")
        bg_color = "lightgreen"
        title = Label(self.root, text="Bill-Dashboard", font=('times new roman', 30, 'bold'), pady=2, bd=12,
                      bg="lightgreen",fg="Black", relief=GROOVE)
        title.pack(fill=X)
    # ================variables=======================
        self.medicine_name = StringVar()
        self.medicine_name1 = StringVar()
        self.medicine_name2 = StringVar()
        self.medicine_name3 = StringVar()

        self.medicine_qty = IntVar()
        self.medicine_qty1=IntVar()
        self.medicine_qty2 = IntVar()
        self.medicine_qty3 = IntVar()

        self.medicine_price = IntVar()
        self.medicine_price1 = IntVar()
        self.medicine_price2 = IntVar()
        self.medicine_price3 = IntVar()

        self.medicine_amount=IntVar()
        self.medicine_amount1 = IntVar()
        self.medicine_amount2 = IntVar()
        self.medicine_amount3 = IntVar()

        self.total_var = IntVar()
        self.total_var1 = IntVar()
        self.total_var2 = IntVar()
        self.total_var3 = IntVar()

        self.total_payable=StringVar()
        self.discount=StringVar()
        self.cgst = StringVar()
        self.sgst = StringVar()
    # ==============Customer==========================
        self.p_name = StringVar()
        self.p_phone = StringVar()
        self.p_dob=StringVar()
        self.p_add=StringVar()
        self.p_sx=StringVar()
        self.p_bill_no = StringVar()
        x = random.randint(500, 999)
        self.p_bill_no.set(str(x))
        self.curr_date = StringVar()

    # =============customer retail details======================
        F1 = LabelFrame(self.root, text="Customer Details", font=('times new roman', 15, 'bold'), bd=7,
                        fg="Black", bg="lightgreen")
        F1.place(x=0, y=75,width=1280,height=130)
        patient_name = Label(F1, text="Patient Name:", bg=bg_color, font=('times new roman', 15, 'bold'))
        patient_name.grid(row=0, column=0, padx=20, pady=5)
        patient_name_en = Entry(F1, width=15, textvariable=self.p_name, font='arial 15', bd=7, relief=GROOVE)
        patient_name_en.grid(row=0, column=1, pady=5, padx=10)

        patient_mob = Label(F1, text="Address:", bg="lightgreen", font=('times new roman', 15, 'bold'))
        patient_mob.grid(row=0, column=2, padx=20, pady=5)
        patient_mob_en = Entry(F1, width=15, textvariable=self.p_phone, font='arial 15', bd=7, relief=GROOVE)
        patient_mob_en.grid(row=0, column=3, pady=5, padx=10)

        p_dob = Label(F1, text="DoB:", bg="lightgreen", font=('times new roman', 15, 'bold'))
        p_dob.grid(row=0, column=4, padx=20, pady=5)
        p_dob_en = Entry(F1, width=15, textvariable=self.p_dob, font='arial 15', bd=7, relief=GROOVE)
        p_dob_en.grid(row=0, column=5, pady=5, padx=10)

        p_add = Label(F1, text="Mobile:", bg="lightgreen", font=('times new roman', 15, 'bold'))
        p_add.grid(row=0, column=6, pady=5, padx=10)
        p_add_en = Entry(F1, width=15, textvariable=self.p_add, font='arial 15', bd=7, relief=GROOVE)
        p_add_en.grid(row=0, column=7, pady=5, padx=10)


        p_sx = Label(F1, text="Sex:", bg="lightgreen", font=('times new roman', 15, 'bold'))
        p_sx.grid(row=1, column=0, padx=20, pady=5)
        p_sx_en = Entry(F1, width=15, textvariable=self.p_sx, font='arial 15', bd=7, relief=GROOVE)
        p_sx_en.grid(row=1, column=1, pady=5, padx=10)

        p_bill = Label(F1, text="Bill No.:", bg="lightgreen", font=('times new roman', 15, 'bold'))
        p_bill.grid(row=1, column=2, padx=20, pady=5)
        p_bill_en = Entry(F1, width=15, textvariable=self.p_bill_no, font='arial 15', bd=7, relief=GROOVE)
        p_bill_en.grid(row=1, column=3, pady=5, padx=10)

        p_curr_date = Label(F1, text="Current Date:", bg="lightgreen", font=('times new roman', 15, 'bold'))
        p_curr_date.grid(row=1, column=4, padx=20, pady=5)
        p_curr_en = Entry(F1, width=15, textvariable=self.curr_date, font='arial 15', bd=7, relief=GROOVE)
        p_curr_en.grid(row=1, column=5, pady=5, padx=10)

    # ===================Medical====================================
        F2 = LabelFrame(self.root, text="Medicine Name", font=('times new roman', 16, 'bold'), bd=10, fg="Black",bg="lightgreen")
        F2.place(x=0, y=205, width=940, height=300)

        medi_name = Label(F2, text="Medicine Name", font=('times new roman', 14, 'bold'), bg="lightgreen",fg="black")
        medi_name.grid(row=0, column=0, padx=20, pady=0, sticky='W')
        qty_en=Entry(F2,width=10,textvariable=self.medicine_name,font=('times new roman',14,'bold'),bd=5,relief=GROOVE)
        qty_en.grid(row=1,column=0,padx=30,pady=10)
        qty_en = Entry(F2, width=10, textvariable=self.medicine_name1, font=('times new roman', 14, 'bold'), bd=5, relief=GROOVE)
        qty_en.grid(row=2, column=0, padx=10, pady=10)
        qty_en = Entry(F2, width=10, textvariable=self.medicine_name2, font=('times new roman', 14, 'bold'), bd=5, relief=GROOVE)
        qty_en.grid(row=3, column=0, padx=10, pady=10)
        qty_en = Entry(F2, width=10, textvariable=self.medicine_name3, font=('times new roman', 14, 'bold'), bd=5, relief=GROOVE)
        qty_en.grid(row=4, column=0, padx=10, pady=10)


        qty_lbl=Label(F2,text="Qty",font=('times new roman',14,'bold'),bg="lightgreen",fg="Black",bd=5)
        qty_lbl.grid(row=0,column=1,padx=70,pady=10,sticky='W')
        qty_en=Entry(F2,width=5,textvariable=self.medicine_qty,font=('times new roman',14,'bold'),bd=5,relief=GROOVE)
        qty_en.grid(row=1,column=1,padx=30,pady=10)
        qty_en = Entry(F2, width=5, textvariable=self.medicine_qty1, font=('times new roman', 14, 'bold'), bd=5, relief=GROOVE)
        qty_en.grid(row=2, column=1, padx=10, pady=10)
        qty_en = Entry(F2, width=5, textvariable=self.medicine_qty2, font=('times new roman', 14, 'bold'), bd=5, relief=GROOVE)
        qty_en.grid(row=3, column=1, padx=10, pady=10)
        qty_en = Entry(F2, width=5, textvariable=self.medicine_qty3, font=('times new roman', 14, 'bold'), bd=5, relief=GROOVE)
        qty_en.grid(row=4, column=1, padx=10, pady=10)

        price_lbl = Label(F2, text="Price", font=('times new roman', 14, 'bold'), bg="lightgreen", fg="Black", bd=5)
        price_lbl.grid(row=0, column=2, padx=70, pady=10, sticky='W')
        price_en = Entry(F2, width=5, textvariable=self.medicine_price, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        price_en.grid(row=1, column=2, padx=10, pady=10)
        price_en = Entry(F2, width=5, textvariable=self.medicine_price1, font=('times new roman', 14, 'bold'), bd=5, relief=GROOVE)
        price_en.grid(row=2, column=2, padx=10, pady=10)
        price_en = Entry(F2, width=5, textvariable=self.medicine_price2, font=('times new roman', 14, 'bold'), bd=5, relief=GROOVE)
        price_en.grid(row=3, column=2, padx=10, pady=10)
        price_en = Entry(F2, width=5, textvariable=self.medicine_price3, font=('times new roman', 14, 'bold'), bd=5, relief=GROOVE)
        price_en.grid(row=4, column=2, padx=10, pady=10)


        amount_lbl = Label(F2, text="Amount", font=('times new roman', 14, 'bold'), bg="lightgreen", fg="Black", bd=5)
        amount_lbl.grid(row=0, column=3, padx=70, pady=10, sticky='W')
        amount_en = Entry(F2, width=5, textvariable=self.total_var, font=('times new roman', 14, 'bold'), bd=5, relief=GROOVE)
        amount_en.grid(row=1, column=3, padx=10, pady=10)
        amount_en = Entry(F2, width=5, textvariable=self.total_var1, font=('times new roman', 14, 'bold'), bd=5, relief=GROOVE)
        amount_en.grid(row=2, column=3, padx=10, pady=10)
        amount_en = Entry(F2, width=5, textvariable=self.total_var2, font=('times new roman', 14, 'bold'), bd=5, relief=GROOVE)
        amount_en.grid(row=3, column=3, padx=10, pady=10)
        amount_en = Entry(F2, width=5, textvariable=self.total_var3, font=('times new roman', 14, 'bold'), bd=5, relief=GROOVE)
        amount_en.grid(row=4, column=3, padx=10, pady=10)



    # =================BillArea======================
        F3 = Frame(self.root, bd=10, relief=GROOVE)
        F3.place(x=945, y=205, width=330, height=300)

        bill_title = Label(F3, text="Bill Area", font='arial 15 bold', bd=7, relief=GROOVE)
        bill_title.pack(fill=X)
        scroll_y = Scrollbar(F3, orient=VERTICAL)
        self.txtarea = Text(F3, yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH, expand=1)

    # =======================ButtonFrame=============
        F4 = LabelFrame(self.root, text="Bill Area", font=('times new roman', 14, 'bold'), bd=10, fg="Black",
                        bg="lightgreen")
        F4.place(x=0, y=505, width=650,height=145)

        disc_btn=Label(F4,text="Discount",font=('times new roman',14,'bold'),bd=1,fg="black",bg="lightgreen")
        disc_btn.grid(row=0,column=0,padx=10,pady=10)
        dics_en1=Entry(F4,width=10,textvariable=self.discount)
        dics_en1.grid(row=1,column=0,padx=10,pady=10)
        cgst_btn=Label(F4,text="CGST",font=('times new roman',14,'bold'),bd=1,fg="black",bg="lightgreen",padx=20)
        cgst_btn.grid(row=0, column=1,padx=40)
        cgst_en2=Entry(F4,width=10,textvariable=self.cgst)
        cgst_en2.grid(row=1,column=1,padx=10,pady=10)
        cgst_btn = Label(F4, text="SGST", font=('times new roman', 14, 'bold'), bd=1, fg="black", bg="lightgreen",padx=20)
        cgst_btn.grid(row=0, column=2, padx=40)
        cgst_en2 = Entry(F4, width=10,textvariable=self.sgst)
        cgst_en2.grid(row=1, column=2, padx=10, pady=10)
        cgst_btn = Label(F4, text="Payable Amount", font=('times new roman', 14, 'bold'), bd=1, fg="black", bg="lightgreen",padx=20)
        cgst_btn.grid(row=0, column=3, padx=40)
        cgst_en2 = Entry(F4, width=10,textvariable=self.total_payable)
        cgst_en2.grid(row=1, column=3, padx=10, pady=10)
    # =======Buttons-======================================
        F5 = LabelFrame(self.root, text="Generate All", font=('times new roman', 14, 'bold'), bd=10, fg="Black",bg="lightgreen")
        F5.place(x=650, y=505, width=620,height=145)

        total_btn = Button(F5,command=self.total ,text="Total", bg="lightgreen", bd=1, fg="chocolate", pady=5,width=10, font='arial 13 bold')
        total_btn.grid(row=0, column=0,padx=20,pady=30)

        generate_Bill_btn = Button(F5, command=self.bill_area, text="Generate Bill", bd=1, bg="lightgreen",fg="chocolate", pady=5, width=10, font='arial 13 bold')
        generate_Bill_btn.grid(row=0, column=1, padx=20,pady=30)

        clear_btn = Button(F5, command=self.clear_data, text="Clear", bg="lightgreen", bd=1, fg="chocolate", pady=5,width=10, font='arial 13 bold')
        clear_btn.grid(row=0, column=2, padx=20,pady=30)

        exit_btn = Button(F5, command=self.exit_app, text="Exit", bd=1, bg="lightgreen", fg="chocolate", pady=5,width=10, font='arial 13 bold')
        exit_btn.grid(row=0, column=3,padx=20,pady=30)
        self.welcome_bill()

    # def apply_discount(self):
    #     discount_percentage =float(self.discount.get())
    #     total_bill_amount = float(self.total_payable.get())
    #     discount_amount = (discount_percentage / 100) * total_bill_amount
    #     discounted_total = total_bill_amount - discount_amount
    #
    #     self.total_payable.set(f"{discounted_total:.2f}")
    #     self.discount.set(discounted_total)

    def calculate_cgst_sgst(self):
        total_bill_amount = float(self.total_payable.get())
        cgst_rate = 2.3
        sgst_rate = 2.5

        cgst = (total_bill_amount * cgst_rate) / 100
        sgst = (total_bill_amount * sgst_rate) / 100

        self.cgst.set(f"{cgst:.2f}")
        self.sgst.set(f"{sgst:.2f}")
    #================totalBill==========================
    def total(self):
        quantities = [self.medicine_qty.get(), self.medicine_qty1.get(), self.medicine_qty2.get(),
                      self.medicine_qty3.get()]
        prices = [self.medicine_price.get(), self.medicine_price1.get(), self.medicine_price2.get(),
                  self.medicine_price3.get()]
        total_vars = [self.total_var, self.total_var1, self.total_var2, self.total_var3]
        for i in range(4):
            total_result = quantities[i] * prices[i]
            total_vars[i].set(total_result)


        self.var0=self.total_var.get()
        self.var1=self.total_var1.get()
        self.var2=self.total_var2.get()
        self.var3=self.total_var3.get()
        self.total_payable_amount = str(self.var0 + self.var1 + self.var2 + self.var3)
        self.total_payable.set(self.total_payable_amount)
        self.calculate_cgst_sgst()

        # self.apply_discount()

    #==============welcome-bill==============================
    def welcome_bill(self):
        self.txtarea.delete('1.0', END)
        self.txtarea.insert(END, "\t\t\tWelcome Medical Store ")
        patient_info = [
            ("Patient name", self.p_name.get()),
            ("Address", self.p_add.get()),
            ("DoB", self.p_dob.get()),
            ("Mobile No.", self.p_phone.get()),
            ("Sex", self.p_sx.get()),
            ("Bill No.", self.p_bill_no.get()),
            ("Current Date", self.curr_date.get())
        ]
        for label, value in patient_info:
            self.txtarea.insert(END, f"\n{label}:{value}")
        self.txtarea.insert(END, "\n================================")
        self.txtarea.insert(END, "\nMedicine\nName\tQTY\tPrice\tAmount")

        entries = [
            (self.medicine_name.get(), self.medicine_qty.get(), self.medicine_price.get(),self.total_var.get()),
            (self.medicine_name1.get(), self.medicine_qty1.get(), self.medicine_price1.get(),self.total_var1.get()),
            (self.medicine_name2.get(), self.medicine_qty2.get(), self.medicine_price2.get(),self.total_var2.get()),
            (self.medicine_name3.get(), self.medicine_qty3.get(), self.medicine_price3.get(),self.total_var3.get()),
        ]
        for name, qty, price,amount in entries:
            self.txtarea.insert(END, f"\n{name}\t{qty}\t{price}\t{amount}")

    # ========
    def bill_area(self):
        if self.p_name.get() == " " or self.p_phone.get() == " ":
            messagebox.showerror("Error", "Customer Details Are Must")
        elif self.medicine_price.get() == "Rs. 0.0":
            messagebox.showerror("Error", "No Product Purchased")
        else:
            self.welcome_bill()
        self.txtarea.insert(END, f"\n--------------------------------")
        self.txtarea.insert(END, f"\nDiscount:\t\t\t Rs.{self.discount.get()}")
        self.txtarea.insert(END, f"\nCGST:\t\t\t Rs.{self.cgst.get()}")
        self.txtarea.insert(END, f"\nSGST:\t\t\t Rs.{self.sgst.get()}")
        self.txtarea.insert(END,f"\n-----------------------------------")
        self.txtarea.insert(END, f"\nTotal Bill:\t\t\t Rs.{self.total_payable_amount}")
        self.save_bill()

    #=========savebill============================
    def save_bill(self):
        op = messagebox.askyesno("Save Bill", "Do you want to save the bill?")
        if op > 0:
            self.bill_data = self.txtarea.get('1.0', END)
            f1 = open("bills/"+str(self.p_bill_no.get())+".txt", "w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved", f"Bill no:{self.p_bill_no.get()} Saved Successfully")
        else:
           return

    # ===================find_bill================================
    def find_bill(self):
        present = "no"
        for i in os.listdir("bills/"):
            if i.split('.')[0] == self.search_bill.get():
                f1 = open(f"bills/{i}", "r")
                self.txtarea.delete("1.0", END)
                for d in f1:
                    self.txtarea.insert(END, d)
                    f1.close()
                present = "yes"
        if present == "no":
            messagebox.showerror("Error", "Invalid Bill No")

    # ======================clear-bill======================
    def clear_data(self):
        op = messagebox.askyesno("Clear", "Do you really want to Clear?")
        if op > 0:
            self.p_name.set("")
            self.p_bill_no.set("")

            self.p_bill_no.set("")
            x = random.randint(1000, 9999)
            self.p_bill_no.set(str(x))

            # self.search_bill.set("")
            self.welcome_bill()

    # ===========exit=======================
    def exit_app(self):
        self.root.destroy()





root = Tk()
obj = Bill_App(root)
root.mainloop()
