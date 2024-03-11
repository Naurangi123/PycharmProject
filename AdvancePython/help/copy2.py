import tkinter as tk
from tkinter import ttk


def calculate_total():
    try:
        var1 = float(entry_var1.get())
        var2 = float(entry_var2.get())
        var3 = float(entry_var3.get())

        total = var1 + var2 + var3
        result_label.config(text=f'Total: {total}')
    except ValueError:
        result_label.config(text='Please enter valid numbers for all variables.')


# Create the main window
root = tk.Tk()
root.title('Variable Calculator')

# Create and place entry widgets for the three variables
label_var1 = ttk.Label(root, text='Variable 1:')
label_var1.grid(row=0, column=0, padx=5, pady=5, sticky='e')
entry_var1 = ttk.Entry(root)
entry_var1.grid(row=0, column=1, padx=5, pady=5)

label_var2 = ttk.Label(root, text='Variable 2:')
label_var2.grid(row=1, column=0, padx=5, pady=5, sticky='e')
entry_var2 = ttk.Entry(root)
entry_var2.grid(row=1, column=1, padx=5, pady=5)

label_var3 = ttk.Label(root, text='Variable 3:')
label_var3.grid(row=2, column=0, padx=5, pady=5, sticky='e')
entry_var3 = ttk.Entry(root)
entry_var3.grid(row=2, column=1, padx=5, pady=5)

# Create a button to calculate the total
calculate_button = ttk.Button(root, text='Calculate Total', command=calculate_total)
calculate_button.grid(row=3, column=0, columnspan=2, pady=10)

# Create a label to display the total
result_label = ttk.Label(root, text='Total: ')
result_label.grid(row=4, column=0, columnspan=2)

# Run the Tkinter event loop
root.mainloop()
