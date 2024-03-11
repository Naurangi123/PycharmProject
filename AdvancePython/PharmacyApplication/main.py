from tkinter import *
from datetime import *
import random



class Pharmacy:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1450x700+0+0")
        self.root.title("Pharmacy Application")
        #==================buyer variable============================
        self.b_name=StringVar()
        self.b_addr=StringVar()
        self.b_contact=StringVar()
        self.b_gst_no=StringVar()
        #===================Invoice==============================
        self.invoice_no=StringVar()
        inv = random.randint(0, 99)
        self.invoice_no.set(str(inv))
        self.b_bill_no = StringVar()
        x = random.randint(0, 99)
        self.b_bill_no.set(str(x))
        self.curr_date=StringVar()
        d=datetime.now()
        formatted_date = d.strftime("%d-%m-%Y / %H:%M")
        self.curr_date.set(str(formatted_date))

        self.payment_mode=StringVar()
        self.c1=IntVar()
        self.c2=IntVar()


        #======================Owner Details ========================================

        F1 = Label(self.root, font='arial 15 bold', bd=5, relief=GROOVE)
        F1.place(x=10,y=10,width=320,height=200)
        scroll_y1 = Scrollbar(F1, orient=VERTICAL)
        self.txtarea1 = Text(F1, yscrollcommand=scroll_y1.set)
        scroll_y1.pack(side=RIGHT, fill=Y)
        scroll_y1.config(command=self.txtarea1.yview)
        self.txtarea1.pack(fill=BOTH, expand=1)
        self.txtarea1.delete('1.0', END)
        self.txtarea1.insert(END, "\n  Sapna Pharmacy & Medical Store")
        # self.txtarea1.insert(END,)
        # self.txtarea1.insert(END)
        # self.txtarea1.insert(END)
        # self.txtarea1.insert(END)
        # self.txtarea1.insert(END)



    #=============================Buyer Details =====================================

        F2 = Label(self.root, font='arial 15 bold', bd=5, relief=GROOVE)
        F2.place(x=330, y=10, width=320, height=200)
        scroll_y2 = Scrollbar(F2, orient=VERTICAL)
        self.txtarea2 = Text(F2, yscrollcommand=scroll_y2.set)
        scroll_y2.pack(side=RIGHT, fill=Y)
        scroll_y2.config(command=self.txtarea2.yview)
        self.txtarea2.pack(fill=BOTH, expand=1)

        F4 = LabelFrame(self.root, text="Buyer Details", bg="chocolate", relief=GROOVE)
        F4.place(x=10, y=215, width=250, height=220)

        b_name = Label(F4, text="Buyer Name:", bg="chocolate")
        b_name.grid(row=0, column=0, padx=10, pady=10)
        b_en1 = Entry(F4, width=8, textvariable=self.b_name)
        b_en1.grid(row=0, column=1, padx=10, pady=10)

        b_name = Label(F4, text="Address:", bg="chocolate")
        b_name.grid(row=1, column=0, padx=10, pady=10)
        b_en1 = Entry(F4, width=8, textvariable=self.b_addr)
        b_en1.grid(row=1, column=1, padx=10, pady=10)

        b_name = Label(F4, text="Contact No. :", bg="chocolate")
        b_name.grid(row=2, column=0, padx=10, pady=10)
        b_en1 = Entry(F4, width=8, textvariable=self.b_contact)
        b_en1.grid(row=2, column=1, padx=10, pady=10)

        b_name = Label(F4, text="GST No.:", bg="chocolate")
        b_name.grid(row=3, column=0, padx=10, pady=10)
        b_en1 = Entry(F4, width=8, textvariable=self.b_gst_no)
        b_en1.grid(row=3, column=1, padx=10, pady=10)
        self.insertDetails()
    def insertDetails(self):
        self.txtarea2.delete('1.0', END)
        self.txtarea2.insert(END, "\n\t\tBuyer Details")
        b_info = [
            ("Buyer Name", self.b_name.get()),
            ("Address", self.b_addr.get()),
            ("Contact No.", self.b_contact.get()),
            ("GST No.", self.b_gst_no.get())
        ]
        for label, value in b_info:
            self.txtarea2.insert(END, f"\n{label}: {value}")

        #=================================Invoice========================

        F3 = Label(self.root, font='arial 15 bold',bd=3, relief=GROOVE)
        F3.place(x=650, y=10, width=320, height=200)
        inv_title = Label(F3, bg="Grey",text="INVOICE", font='system 15 bold', bd=2, relief=GROOVE)
        inv_title.pack(fill=X)
        scroll_y3 = Scrollbar(F3, orient=VERTICAL)
        self.txtarea3 = Text(F3, yscrollcommand=scroll_y3.set)
        scroll_y3.pack(side=RIGHT, fill=Y)
        scroll_y3.config(command=self.txtarea3.yview)
        self.txtarea3.pack(fill=BOTH, expand=1)
        self.txtarea3.delete('1.0', END)
        self.txtarea3.insert(END, f"\nInvoice No. {self.invoice_no.get()}")
        self.txtarea3.insert(END, f"\nBill No. {self.b_bill_no.get()}")
        self.txtarea3.insert(END, f"\nCurrent Date : {self.curr_date.get()}")
        self.txtarea3.insert(END, f"\nPayment Mode :Online Mode📱\n\t\tCash Mode💰")
        self.txtarea3.insert(END,"\nNote: Remarks")

        # F4 = Label(self.root, font='arial 15 bold', bd=5, relief=GROOVE)
        # F4.place(x=10, y=440, width=350, height=200)
        # scroll_y4 = Scrollbar(F4, orient=VERTICAL)
        # self.txtarea4 = Text(F4, yscrollcommand=scroll_y4.set)
        # scroll_y4.pack(side=RIGHT, fill=Y)
        # scroll_y4.config(command=self.txtarea1.yview)
        # self.txtarea4.pack(fill=BOTH, expand=1)
        # self.txtarea4.delete('1.0', END)
        # self.txtarea4.insert(END, "\n Bank details ")
        #
        # F5 = Label(self.root, font='arial 15 bold', bd=5, relief=GROOVE)
        # F5.place(x=360, y=440, width=520, height=200)
        # scroll_y5 = Scrollbar(F5, orient=VERTICAL)
        # self.txtarea5 = Text(F5, yscrollcommand=scroll_y5.set)
        # scroll_y5.pack(side=RIGHT, fill=Y)
        # scroll_y5.config(command=self.txtarea1.yview)
        # self.txtarea5.pack(fill=BOTH, expand=1)
        # self.txtarea5.delete('1.0', END)
        # self.txtarea5.insert(END, "\n Bill Amount")
        #
        # F6 = Label(self.root, font='arial 15 bold', bd=5, relief=GROOVE)
        # F6.place(x=880, y=440, width=320, height=200)
        # scroll_y6 = Scrollbar(F6, orient=VERTICAL)
        # self.txtarea6 = Text(F6, yscrollcommand=scroll_y6.set)
        # scroll_y6.pack(side=RIGHT, fill=Y)
        # scroll_y6.config(command=self.txtarea1.yview)
        # self.txtarea6.pack(fill=BOTH, expand=1)
        # self.txtarea6.delete('1.0', END)
        # self.txtarea6.insert(END,"\n Total Bill Amount ")

        F5=Frame(self.root,padx=10,pady=5)
        F5.place(x=1200,y=580)
        btn=Button(F5,command=self.insertDetails,text="Submit",bg="red",padx=5,pady=10)
        btn.grid(row=0,column=0)



root=Tk()
obj=Pharmacy(root)
root.mainloop()