from tkinter import *
from tkinter import messagebox
import random
class Entryfrom:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1450x700+0+0")
        self.root.title("Entry Form")

        self.total_payable=StringVar()

        #======================MEDICINE VARIABLES===================
        self.medi_name1 = StringVar()
        self.medi_name2 = StringVar()
        self.medi_name3 = StringVar()
        self.medi_name4 = StringVar()
        self.medi_name5 = StringVar()
        self.medi_name6 = StringVar()
        self.medi_name7 = StringVar()
        self.medi_name8 = StringVar()
        self.medi_name9 = StringVar()
        self.medi_name10 = StringVar()
        self.medi_name11= StringVar()
        self.medi_name12= StringVar()
        self.medi_name13 = StringVar()
        self.medi_name14 = StringVar()

        #======================QTY VARIABLES=========================

        self.qty1 = IntVar()# convert all into IntVar
        self.qty2 = IntVar()
        self.qty3 = IntVar()
        self.qty4 = IntVar()
        self.qty5 = IntVar()
        self.qty6 = IntVar()
        self.qty7 = IntVar()
        self.qty8 = IntVar()
        self.qty9 = IntVar()
        self.qty10 = IntVar()
        self.qty11 = IntVar()
        self.qty12 = IntVar()
        self.qty13 = IntVar()
        self.qty14 = IntVar()

        #======================PRICE VARIABLES====================================

        self.price1 = IntVar() # convert it Into IntVar
        self.price2 = IntVar()
        self.price3 = IntVar()
        self.price4 = IntVar()
        self.price5 = IntVar()
        self.price6 = IntVar()
        self.price7 = IntVar()
        self.price8 = IntVar()
        self.price9 = IntVar()
        self.price10 = IntVar()
        self.price11 = IntVar()
        self.price12 = IntVar()
        self.price13 = IntVar()
        self.price14 = IntVar()

        #=====================GST VARIABLES==================================

        self.gst = IntVar()



        #=======================SGST VARIABLES===================================
        self.sgst=IntVar()

        #========================CGST VARIABLES========================================

        self.cgst = IntVar()

        #==========================QTY*PRICE VARIABLES=======================
        self.total_var1 = IntVar()
        self.total_var2 = IntVar()
        self.total_var3 = IntVar()
        self.total_var4 = IntVar()
        self.total_var5= IntVar()
        self.total_var6 = IntVar()
        self.total_var7 = IntVar()
        self.total_var8 = IntVar()
        self.total_var9 = IntVar()
        self.total_var10 = IntVar()
        self.total_var11 = IntVar()
        self.total_var12 = IntVar()
        self.total_var13 = IntVar()
        self.total_var14 = IntVar()


        #======================================== FRAME ==================================
        F1 = LabelFrame(self.root, text="Buyer Details", bg="orange", relief=GROOVE)
        F1.place(x=0, y=5, width=820, height=640)


        medicine_lbl = Label(F1, text="Medicine Name:", bg="orange")
        medicine_lbl.grid(row=0, column=0, padx=20, pady=10)
        m_en1 = Entry(F1, width=15,textvariable=self.medi_name1)
        m_en1.grid(row=1, column=0, padx=10, pady=10)
        m_en2 = Entry(F1, width=15,textvariable=self.medi_name2)
        m_en2.grid(row=2, column=0, padx=10, pady=10)
        m_en3 = Entry(F1, width=15,textvariable=self.medi_name3)
        m_en3.grid(row=3, column=0, padx=10, pady=10)
        m_en4 = Entry(F1, width=15,textvariable=self.medi_name4)
        m_en4.grid(row=4, column=0, padx=10, pady=10)
        m_en5 = Entry(F1, width=15,textvariable=self.medi_name5)
        m_en5.grid(row=5, column=0, padx=10, pady=10)
        m_en6 = Entry(F1, width=15,textvariable=self.medi_name6)
        m_en6.grid(row=6, column=0, padx=10, pady=10)
        m_en7 = Entry(F1, width=15,textvariable=self.medi_name7)
        m_en7.grid(row=7, column=0, padx=10, pady=10)
        m_en8 = Entry(F1, width=15,textvariable=self.medi_name8)
        m_en8.grid(row=8, column=0, padx=10, pady=10)
        m_en9 = Entry(F1, width=15,textvariable=self.medi_name9)
        m_en9.grid(row=9, column=0, padx=10, pady=10)
        m_en10 = Entry(F1, width=15,textvariable=self.medi_name10)
        m_en10.grid(row=10, column=0, padx=10, pady=10)
        m_en11 = Entry(F1, width=15,textvariable=self.medi_name11)
        m_en11.grid(row=11, column=0, padx=10, pady=10)
        m_en12 = Entry(F1, width=15,textvariable=self.medi_name12)
        m_en12.grid(row=12, column=0, padx=10, pady=10)
        m_en13 = Entry(F1, width=15,textvariable=self.medi_name13)
        m_en13.grid(row=13, column=0, padx=10, pady=10)
        m_en14 = Entry(F1, width=15,textvariable=self.medi_name14)
        m_en14.grid(row=14, column=0, padx=10, pady=10)

    #========================Quality==========================

        qty_lbl = Label(F1, text="Quality", bg="orange")
        qty_lbl.grid(row=0, column=1, padx=30, pady=10)
        q_en1 = Entry(F1, width=15,textvariable=self.qty1)
        q_en1.grid(row=1, column=1, padx=10, pady=10)
        q_en2 = Entry(F1, width=15,textvariable=self.qty2)
        q_en2.grid(row=2, column=1, padx=10, pady=10)
        q_en3 = Entry(F1, width=15,textvariable=self.qty3)
        q_en3.grid(row=3, column=1, padx=10, pady=10)
        q_en4 = Entry(F1, width=15,textvariable=self.qty4)
        q_en4.grid(row=4, column=1, padx=10, pady=10)
        q_en5 = Entry(F1, width=15,textvariable=self.qty5)
        q_en5.grid(row=5, column=1, padx=10, pady=10)
        q_en6 = Entry(F1, width=15,textvariable=self.qty6)
        q_en6.grid(row=6, column=1, padx=10, pady=10)
        q_en7 = Entry(F1, width=15,textvariable=self.qty7)
        q_en7.grid(row=7, column=1, padx=10, pady=10)
        q_en8 = Entry(F1, width=15,textvariable=self.qty8)
        q_en8.grid(row=8, column=1, padx=10, pady=10)
        q_en9 = Entry(F1, width=15,textvariable=self.qty9)
        q_en9.grid(row=9, column=1, padx=10, pady=10)
        q_en10 = Entry(F1, width=15,textvariable=self.qty10)
        q_en10.grid(row=10, column=1, padx=10, pady=10)
        q_en11 = Entry(F1, width=15,textvariable=self.qty11)
        q_en11.grid(row=11, column=1, padx=10, pady=10)
        q_en12 = Entry(F1, width=15,textvariable=self.qty12)
        q_en12.grid(row=12, column=1, padx=10, pady=10)
        q_en13 = Entry(F1, width=15,textvariable=self.qty13)
        q_en13.grid(row=13, column=1, padx=10, pady=10)
        q_en14 = Entry(F1, width=15,textvariable=self.qty14)
        q_en14.grid(row=14, column=1, padx=10, pady=10)

        #========================= Price==========================

        p_lbl = Label(F1, text="Price", bg="orange")
        p_lbl.grid(row=0, column=2, padx=20, pady=10)
        p_en1 = Entry(F1, width=15,textvariable=self.price1)
        p_en1.grid(row=1, column=2, padx=10, pady=10)
        p_en2 = Entry(F1, width=15,textvariable=self.price2)
        p_en2.grid(row=2, column=2, padx=10, pady=10)
        p_en3 = Entry(F1, width=15,textvariable=self.price3)
        p_en3.grid(row=3, column=2, padx=10, pady=10)
        p_en4 = Entry(F1, width=15,textvariable=self.price4)
        p_en4.grid(row=4, column=2, padx=10, pady=10)
        p_en5 = Entry(F1, width=15,textvariable=self.price5)
        p_en5.grid(row=5, column=2, padx=10, pady=10)
        p_en6 = Entry(F1, width=15,textvariable=self.price6)
        p_en6.grid(row=6, column=2, padx=10, pady=10)
        p_en7 = Entry(F1, width=15,textvariable=self.price7)
        p_en7.grid(row=7, column=2, padx=10, pady=10)
        p_en8 = Entry(F1, width=15,textvariable=self.price8)
        p_en8.grid(row=8, column=2, padx=10, pady=10)
        p_en9 = Entry(F1, width=15,textvariable=self.price9)
        p_en9.grid(row=9, column=2, padx=10, pady=10)
        p_en10 = Entry(F1, width=15,textvariable=self.price10)
        p_en10.grid(row=10, column=2, padx=10, pady=10)
        p_en11 = Entry(F1, width=15,textvariable=self.price11)
        p_en11.grid(row=11, column=2, padx=10, pady=10)
        p_en12 = Entry(F1, width=15,textvariable=self.price12)
        p_en12.grid(row=12, column=2, padx=10, pady=10)
        p_en13 = Entry(F1, width=15,textvariable=self.price13)
        p_en13.grid(row=13, column=2, padx=10, pady=10)
        p_en14 = Entry(F1, width=15,textvariable=self.price14)
        p_en14.grid(row=14, column=2, padx=10, pady=10)

        #================================ GST========================
        gst_lbl = Label(F1, text="GST", bg="orange")
        gst_lbl.grid(row=0, column=3, padx=20, pady=10)
        g_en1 = Entry(F1, width=15,textvariable=self.gst)
        g_en1.grid(row=1, column=3, padx=10, pady=10)
        g_en2 = Entry(F1, width=15,textvariable=self.gst)
        g_en2.grid(row=2, column=3, padx=10, pady=10)
        g_en3 = Entry(F1, width=15,textvariable=self.gst)
        g_en3.grid(row=3, column=3, padx=10, pady=10)
        g_en4 = Entry(F1, width=15,textvariable=self.gst)
        g_en4.grid(row=4, column=3, padx=10, pady=10)
        g_en5 = Entry(F1, width=15,textvariable=self.gst)
        g_en5.grid(row=5, column=3, padx=10, pady=10)
        g_en6 = Entry(F1, width=15,textvariable=self.gst)
        g_en6.grid(row=6, column=3, padx=10, pady=10)
        g_en7 = Entry(F1, width=15,textvariable=self.gst)
        g_en7.grid(row=7, column=3, padx=10, pady=10)
        g_en8 = Entry(F1, width=15,textvariable=self.gst)
        g_en8.grid(row=8, column=3, padx=10, pady=10)
        g_en9 = Entry(F1, width=15,textvariable=self.gst)
        g_en9.grid(row=9, column=3, padx=10, pady=10)
        g_en10 = Entry(F1, width=15,textvariable=self.gst)
        g_en10.grid(row=10, column=3, padx=10, pady=10)
        g_en11 = Entry(F1, width=15,textvariable=self.gst)
        g_en11.grid(row=11, column=3, padx=10, pady=10)
        g_en12 = Entry(F1, width=15,textvariable=self.gst)
        g_en12.grid(row=12, column=3, padx=10, pady=10)
        g_en13 = Entry(F1, width=15,textvariable=self.gst)
        g_en13.grid(row=13, column=3, padx=10, pady=10)
        g_en14 = Entry(F1, width=15,textvariable=self.gst)
        g_en14.grid(row=14, column=3, padx=10, pady=10)

        #===============================CGST============================
        cgst_lbl = Label(F1, text="CGST", bg="orange")
        cgst_lbl.grid(row=0, column=4, padx=20, pady=10)
        c_en1 = Entry(F1, width=15,textvariable=self.cgst)
        c_en1.grid(row=1, column=4, padx=10, pady=10)
        c_en2 = Entry(F1, width=15,textvariable=self.cgst)
        c_en2.grid(row=2, column=4, padx=10, pady=10)
        c_en3 = Entry(F1, width=15,textvariable=self.cgst)
        c_en3.grid(row=3, column=4, padx=10, pady=10)
        c_en4 = Entry(F1, width=15,textvariable=self.cgst)
        c_en4.grid(row=4, column=4, padx=10, pady=10)
        c_en5 = Entry(F1, width=15,textvariable=self.cgst)
        c_en5.grid(row=5, column=4, padx=10, pady=10)
        c_en6 = Entry(F1, width=15,textvariable=self.cgst)
        c_en6.grid(row=6, column=4, padx=10, pady=10)
        c_en7 = Entry(F1, width=15,textvariable=self.cgst)
        c_en7.grid(row=7, column=4, padx=10, pady=10)
        c_en8 = Entry(F1, width=15,textvariable=self.cgst)
        c_en8.grid(row=8, column=4, padx=10, pady=10)
        c_en9 = Entry(F1, width=15,textvariable=self.cgst)
        c_en9.grid(row=9, column=4, padx=10, pady=10)
        c_en10 = Entry(F1, width=15,textvariable=self.cgst)
        c_en10.grid(row=10, column=4, padx=10, pady=10)
        c_en11 = Entry(F1, width=15,textvariable=self.cgst)
        c_en11.grid(row=11, column=4, padx=10, pady=10)
        c_en12 = Entry(F1, width=15,textvariable=self.cgst)
        c_en12.grid(row=12, column=4, padx=10, pady=10)
        c_en13 = Entry(F1, width=15,textvariable=self.cgst)
        c_en13.grid(row=13, column=4, padx=10, pady=10)
        c_en14 = Entry(F1, width=15,textvariable=self.cgst)
        c_en14.grid(row=14, column=4, padx=10, pady=10)

        #=============================SGST============================
        sgst_lbl = Label(F1, text="SGST", bg="orange")
        sgst_lbl.grid(row=0, column=5, padx=20, pady=10)
        s_en1 = Entry(F1, width=15,textvariable=self.sgst)
        s_en1.grid(row=1, column=5, padx=10, pady=10)
        s_en2 = Entry(F1, width=15,textvariable=self.sgst)
        s_en2.grid(row=2, column=5, padx=10, pady=10)
        s_en3 = Entry(F1, width=15,textvariable=self.sgst)
        s_en3.grid(row=3, column=5, padx=10, pady=10)
        s_en4 = Entry(F1, width=15,textvariable=self.sgst)
        s_en4.grid(row=4, column=5, padx=10, pady=10)
        s_en5 = Entry(F1, width=15,textvariable=self.sgst)
        s_en5.grid(row=5, column=5, padx=10, pady=10)
        s_en6 = Entry(F1, width=15,textvariable=self.sgst)
        s_en6.grid(row=6, column=5, padx=10, pady=10)
        s_en7 = Entry(F1, width=15,textvariable=self.sgst)
        s_en7.grid(row=7, column=5, padx=10, pady=10)
        s_en8 = Entry(F1, width=15,textvariable=self.sgst)
        s_en8.grid(row=8, column=5, padx=10, pady=10)
        s_en9 = Entry(F1, width=15,textvariable=self.sgst)
        s_en9.grid(row=9, column=5, padx=10, pady=10)
        s_en10 = Entry(F1, width=15,textvariable=self.sgst)
        s_en10.grid(row=10, column=5, padx=10, pady=10)
        s_en11 = Entry(F1, width=15,textvariable=self.sgst)
        s_en11.grid(row=11, column=5, padx=10, pady=10)
        s_en12 = Entry(F1, width=15,textvariable=self.sgst)
        s_en12.grid(row=12, column=5, padx=10, pady=10)
        s_en13 = Entry(F1, width=15,textvariable=self.sgst)
        s_en13.grid(row=13, column=5, padx=10, pady=10)
        s_en14 = Entry(F1, width=15,textvariable=self.sgst)
        s_en14.grid(row=14, column=5, padx=10, pady=10)

        #============================Amount============================
        amount_lbl = Label(F1, text="Amount:", bg="orange")
        amount_lbl.grid(row=0, column=6, padx=20, pady=10)
        a_en1 = Entry(F1, width=15,textvariable=self.total_var1)
        a_en1.grid(row=1, column=6, padx=10, pady=10)
        a_en2 = Entry(F1, width=15,textvariable=self.total_var2)
        a_en2.grid(row=2, column=6, padx=10, pady=10)
        a_en3 = Entry(F1, width=15,textvariable=self.total_var3)
        a_en3.grid(row=3, column=6, padx=10, pady=10)
        a_en4 = Entry(F1, width=15,textvariable=self.total_var4)
        a_en4.grid(row=4, column=6, padx=10, pady=10)
        a_en5 = Entry(F1, width=15,textvariable=self.total_var5)
        a_en5.grid(row=5, column=6, padx=10, pady=10)
        a_en6 = Entry(F1, width=15,textvariable=self.total_var6)
        a_en6.grid(row=6, column=6, padx=10, pady=10)
        a_en7 = Entry(F1, width=15,textvariable=self.total_var7)
        a_en7.grid(row=7, column=6, padx=10, pady=10)
        a_en8 = Entry(F1, width=15,textvariable=self.total_var8)
        a_en8.grid(row=8, column=6, padx=10, pady=10)
        a_en9 = Entry(F1, width=15,textvariable=self.total_var9)
        a_en9.grid(row=9, column=6, padx=10, pady=10)
        a_en10 = Entry(F1, width=15,textvariable=self.total_var10)
        a_en10.grid(row=10, column=6, padx=10, pady=10)
        a_en11 = Entry(F1, width=15,textvariable=self.total_var11)
        a_en11.grid(row=11, column=6, padx=10, pady=10)
        a_en12 = Entry(F1, width=15,textvariable=self.total_var12)
        a_en12.grid(row=12, column=6, padx=10, pady=10)
        a_en13 = Entry(F1, width=15,textvariable=self.total_var13)
        a_en13.grid(row=13, column=6, padx=10, pady=10)
        a_en14 = Entry(F1, width=15,textvariable=self.total_var14)
        a_en14.grid(row=14, column=6, padx=10, pady=10)

        F3 = Label(self.root, font='arial 15 bold', bg="orange", bd=5, relief=GROOVE)
        F3.place(x=820, y=590, width=450, height=50)


        sbmt_btn = Button(F3, command=self.total, text="Submit", width=6, padx=5, pady=5)
        sbmt_btn.grid(row=0, column=0,padx=25,pady=2)

        sbmt_btn = Button(F3, command=self.bill_area, text="Bill", width=6, padx=5, pady=5)
        sbmt_btn.grid(row=0, column=1,padx=25,pady=2)

        bl_btn = Button(F3, command=self.save_bill, text="Save", bg="red", width=6, padx=5, pady=5)
        bl_btn.grid(row=0, column=2 ,padx=25,pady=2)

        bl_btn = Button(F3, command=self.exit_app, text="Exit", bg="red", width=6, padx=5, pady=5)
        bl_btn.grid(row=0, column=3, padx=25, pady=2)


        F2 = Label(self.root, font='arial 15 bold', bd=5,bg='green', relief=GROOVE)
        F2.place(x=820, y=8, width=450, height=580)
        scroll_y = Scrollbar(F2, orient=VERTICAL)
        self.txtarea = Text(F2, yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.txtarea.yview)
        scroll_x = Scrollbar(F2, orient=HORIZONTAL)
        self.txtarea = Text(F2, xscrollcommand=scroll_x.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_x.config(command=self.txtarea.xview)
        self.txtarea.pack(fill=BOTH, expand=1)
        self.bill_area()


    def welcome_bill(self):
        self.txtarea.delete(2.0, END)
        self.txtarea.insert(END, "\n\t\t Medicine details")
        self.txtarea.insert(END, f"\nmedicine\t\tQty\t\tPrice\t\tAmount")
        entries = [
            (self.medi_name1.get(), self.qty1.get(), self.price1.get(),self.total_var1.get()),
            (self.medi_name2.get(), self.qty2.get(), self.price2.get(),self.total_var2.get()),
            (self.medi_name3.get(), self.qty3.get(), self.price3.get(),self.total_var3.get()),
            (self.medi_name4.get(), self.qty4.get(), self.price4.get(),self.total_var4.get()),
            (self.medi_name5.get(), self.qty5.get(), self.price5.get(),self.total_var5.get()),
            (self.medi_name6.get(), self.qty6.get(), self.price6.get(),self.total_var6.get()),
            (self.medi_name7.get(), self.qty7.get(), self.price7.get(),self.total_var7.get()),
            (self.medi_name8.get(), self.qty8.get(), self.price8.get(),self.total_var8.get()),
            (self.medi_name8.get(), self.qty9.get(), self.price9.get(),self.total_var9.get()),
            (self.medi_name10.get(), self.qty10.get(), self.price10.get(),self.total_var10.get()),
            (self.medi_name11.get(), self.qty11.get(), self.price11.get(),self.total_var11.get()),
            (self.medi_name12.get(), self.qty12.get(), self.price12.get(),self.total_var12.get()),
            (self.medi_name13.get(), self.qty13.get(), self.price13.get(),self.total_var13.get()),
            (self.medi_name14.get(), self.qty14.get(), self.price14.get(),self.total_var14.get()),
        ]
        for name, qty, price,vars in entries:
            self.txtarea.insert(END, f"\n{name}\t\t{qty}\t\t{price}\t\t{vars}")


    def total(self):
        quantities = [self.qty1.get(), self.qty2.get(), self.qty3.get(), self.qty4.get(),self.qty5.get(),
                      self.qty6.get(), self.qty7.get(), self.qty8.get(),self.qty9.get(), self.qty10.get(),
                      self.qty11.get(), self.qty12.get(),self.qty13.get(), self.qty14.get()]

        prices = [self.price1.get(), self.price2.get(), self.price3.get(),self.price4.get(),self.price5.get(),
                  self.price6.get(), self.price7.get(),self.price8.get(),self.price9.get(), self.price10.get(),
                  self.price11.get(),self.price12.get(),self.price13.get(), self.price14.get()]

        total_vars = [self.total_var1, self.total_var2, self.total_var3, self.total_var4,self.total_var5,
                      self.total_var6,self.total_var7,self.total_var8,self.total_var9,self.total_var10,
                      self.total_var11,self.total_var12,self.total_var13,self.total_var14]

        for i in range(14):
            if quantities[i] and prices[i]:  # Check if quantity and price are not empty
                total_result = quantities[i] * prices[i]
                total_vars[i].set(total_result)

#==========TotalAMOUNT AFTER FINAL ADDITION====================

        self.var1 = self.total_var1.get()
        self.var2 = self.total_var2.get()
        self.var3 = self.total_var3.get()
        self.var4 = self.total_var4.get()
        self.var5 = self.total_var5.get()
        self.var6 = self.total_var6.get()
        self.var7 = self.total_var7.get()
        self.var8 = self.total_var8.get()
        self.var9 = self.total_var9.get()
        self.var10 = self.total_var10.get()
        self.var11= self.total_var11.get()
        self.var12 = self.total_var12.get()
        self.var13= self.total_var13.get()
        self.var14= self.total_var14.get()
        self.total_payable_amount = str(self.var1 + self.var2 + self.var3 + self.var4 + self.var5 + self.var6 +
                                        self.var7 + self.var8 + self.var9 + self.var10 + self.var11 + self.var12 +
                                        self.var13 + self.var14)
        self.total_payable.set(self.total_payable_amount)

    def bill_area(self):
        self.welcome_bill()
        self.sgst_cgst()

    def save_bill(self):
        self.bill_no = random.randint(1, 100)
        op = messagebox.askyesno("Save Bill", "Do you want to save the bill?")
        if op > 0:
            self.bill_data = self.txtarea.get('1.0', END)
            f1 = open("bills/"+str(self.bill_no)+".txt", "w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved", f"Bill no:{self.bill_no} Saved Successfully")
        else:
           return

    def sgst_cgst(self):
        total_bill_amount = 0
        cgst_rate = 2.3
        sgst_rate = 2.5

        cgst = (total_bill_amount * cgst_rate) / 100
        sgst = (total_bill_amount * sgst_rate) / 100

        self.cgst.set(f"{cgst:.2f}")
        self.sgst.set(f"{sgst:.2f}")

    def exit_app(self):
        self.root.destroy()



root = Tk()
obj = Entryfrom(root)
root.mainloop()