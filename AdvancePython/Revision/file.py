import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class DataTable(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Data Table")

        self.table = ttk.Treeview(self, columns=("Name", "Age", "City"), show="headings")
        self.table.heading("Name", text="Name")
        self.table.heading("Age", text="Age")
        self.table.heading("City", text="City")

        self.table.pack(pady=10)

        self.entry_name = tk.Entry(self)
        self.entry_age = tk.Entry(self)
        self.entry_city = tk.Entry(self)

        tk.Label(self, text="Name:").pack()
        self.entry_name.pack()

        tk.Label(self, text="Age:").pack()
        self.entry_age.pack()

        tk.Label(self, text="City:").pack()
        self.entry_city.pack()

        tk.Button(self, text="Add Data", command=self.add_data).pack(pady=10)

    def add_data(self):
        name = self.entry_name.get()
        age = self.entry_age.get()
        city = self.entry_city.get()

        if name and age and city:
            self.table.insert("", "end", values=(name, age, city))
            self.entry_name.delete(0, "end")
            self.entry_age.delete(0, "end")
            self.entry_city.delete(0, "end")
        else:
            tk.messagebox.showwarning("Input Error", "Please enter values for all fields.")

if __name__ == "__main__":
    app = DataTable()
    app.mainloop()
