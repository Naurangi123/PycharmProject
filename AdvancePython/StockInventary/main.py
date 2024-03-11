from reportlab.lib.pagesizes import letter
from reportlab.platypus import Table, TableStyle,SimpleDocTemplate
from reportlab.lib import colors
from tkinter import *
from tkinter import messagebox
import os
import random


#F8DFC5

#8A2BE2
#458B74
# FFE4C4
# Olive
#728316

# Turquoise
#36D6E7

# Tan
#B08B57

class Stock:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1450x700+0+0")
        self.root.title("Stock Inventory")
        #============= variables =======================
        self.medicine = StringVar()
        self.itemtype = StringVar()
        self.qty = StringVar()
        self.price = StringVar()
        self.sgst = StringVar()
        self.cgst = StringVar()
        self.hsn_no = StringVar()
        self.bill_no=IntVar()
        # x = random.randint(1, 99)
        # self.bill_no.set(str(x))
        #============== font_type,font_color,bg_color =======================
        font_type="Serif"
        bg_color="#8A2BE2"
        fg_color="#7FFF00"

        #==============Top Label ==================
        title = Label(self.root, text="Stock-Inventory", font=('system', 30, 'bold'), pady=2, bd=12,
                      bg="#FF4040",fg="green", relief=GROOVE)
        title.pack(fill=X)
        #================
        F1=LabelFrame(self.root,text="Inventory",font=('system', 20, 'bold'),bd=3,bg="#8A2BE2",relief=GROOVE)
        F1.place(x=0,y=73,width=1280,height=110)

        medic_lbl = Label(F1, text="Medicine name:", font=font_type, bg=bg_color, fg=fg_color)
        medic_lbl.grid(row=0, column=0, padx=5, pady=10)
        medic_en1 = Entry(F1, textvariable=self.medicine, width=10)
        medic_en1.grid(row=0, column=1, padx=5, pady=10)

        medic_lbl = Label(F1, text="Price:", font=font_type, bg=bg_color, fg=fg_color)
        medic_lbl.grid(row=0, column=3, padx=5, pady=10)
        medic_en1 = Entry(F1, textvariable=self.price, width=10)
        medic_en1.grid(row=0, column=4, padx=5, pady=10)

        medic_lbl = Label(F1, text="QTY:", font=font_type, bg=bg_color, fg=fg_color)
        medic_lbl.grid(row=0, column=5, padx=5, pady=10)
        medic_en1 = Entry(F1, textvariable=self.qty, width=10)
        medic_en1.grid(row=0, column=6, padx=5, pady=10)

        medic_lbl = Label(F1, text="SGST:", font=font_type, bg=bg_color, fg=fg_color)
        medic_lbl.grid(row=0, column=7, padx=5, pady=10)
        medic_en1 = Entry(F1, textvariable=self.sgst, width=10)
        medic_en1.grid(row=0, column=8, padx=5, pady=10)

        medic_lbl = Label(F1, text="CGST:", font=font_type, bg=bg_color, fg=fg_color)
        medic_lbl.grid(row=0, column=9, padx=5, pady=10)
        medic_en1 = Entry(F1, textvariable=self.cgst, width=10)
        medic_en1.grid(row=0, column=10, padx=5, pady=10)

        medic_lbl = Label(F1, text="HSN No.:", font=font_type, bg=bg_color, fg=fg_color)
        medic_lbl.grid(row=0, column=11, padx=5, pady=10)
        medic_en1 = Entry(F1, textvariable=self.hsn_no, width=10)
        medic_en1.grid(row=0, column=12, padx=5, pady=10)

        medic_lbl = Label(F1, text="Item Name:", font=font_type, bg=bg_color, fg=fg_color)
        medic_lbl.grid(row=0, column=13, padx=5, pady=10)
        medic_en1 = Entry(F1, textvariable=self.itemtype, width=10)
        medic_en1.grid(row=0, column=14, padx=5, pady=10)

        submit_btn = Button(F1, width=10, command=self.submit, text="SUBMIT", font="system", fg="black")
        submit_btn.grid(row=0, column=16, padx=50, pady=20)



        #=============================Bill-Area ======================

        F2 = Frame(self.root, bd=2, relief=GROOVE)
        F2.place(x=0, y=185, width=1280, height=900)
        bill_title = Label(F2, text="Stock-Inventory Items", font=font_type,bg=bg_color, bd=0, relief=GROOVE)
        bill_title.pack(fill=X)
        scroll_y = Scrollbar(F2, orient=VERTICAL)
        self.txtarea = Text(F2, yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH, expand=1)
        self.welcome_bill()
        self.submit()

        F3 = LabelFrame(self.root, bd=0, bg="white", relief=GROOVE)
        F3.place(x=0, y=580, width=1280, height=60)

        save_btn = Button(F3, width=10, command=self.save_bill,bg="#36D6E7", text="SAVE", font="system", bd=5, fg="black", padx=5,
                          pady=5)
        save_btn.grid(row=0, column=11, padx=450, pady=10)

        ext_btn = Button(F3, width=10, command=self.exit_app, text="Exit", font="system", bg="lightgreen", bd=5,
                         fg="red", padx=5, pady=5)
        ext_btn.grid(row=0, column=16, padx=100, pady=10)


    def welcome_bill(self):
        self.bill_no=random.randint(1,100)
        self.txtarea.delete('1.0', END)
        self.txtarea.insert(END, f"\nStock No\n{self.bill_no}\tMedicineName\t\t\tPrice\t\tQTY\t\t\tSGST\t\t\tCGST\t\t\tHSN No.\t\t\tItem Name")

    def submit(self):
        entries=[
            self.medicine.get(),
            self.price.get(),
            self.qty.get(),
            self.sgst.get(),
            self.cgst.get(),
            self.hsn_no.get(),
            self.itemtype.get()
        ]

        display_text = ""
        for entry in entries:
            display_text += f"{entry}\t\t"
        self.txtarea.insert(END, f"\n\t{display_text}")
        self.clear_data()

    def save_bill(self):
        text_file_path = f"bills/ {self.bill_no} Stock_Inventory_Report.txt"
        save_file_content = self.txtarea.get('1.0', END)

        with open(text_file_path, "w") as text_file:
            text_file.write(save_file_content)

        self.create_pdf_table()
        messagebox.showinfo("Saved", "Bill Saved Successfully")
        self.welcome_bill()

    def exit_app(self):
        op = messagebox.askyesno("Exit", "Do you really want to exit?")
        if op > 0:
            self.root.destroy()

    def create_pdf_table(self):
        pdf_file_path = f"PDF/{self.bill_no}_Stock_Inventory_Table.pdf"

        # Extracting data from the text area
        table_data = [line.split() for line in self.txtarea.get("3.0", "end-1c").split("\t\n")]

        modified_data = []
        for row in table_data:
            modified_row = []
            for value in row:
                if value:
                    modified_row.append(value)
                else:
                    modified_row.append(None)
            modified_data.append(modified_row)
        # Generating PDF document
        doc = SimpleDocTemplate(pdf_file_path, pagesize=letter)
        table = Table(modified_data)

        # Add style to the table
        style = TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ])
        table.setStyle(style)

        # Build the PDF document
        elements = [table]
        doc.build(elements)

        messagebox.showinfo("PDF Created", f"PDF file saved at {pdf_file_path}")
    def clear_data(self):
        self.medicine.set(""),
        self.price.set(""),
        self.qty.set(""),
        self.sgst.set(""),
        self.cgst.set(""),
        self.hsn_no.set(""),
        self.itemtype.set("")





root=Tk()
obj=Stock(root)
root.mainloop()