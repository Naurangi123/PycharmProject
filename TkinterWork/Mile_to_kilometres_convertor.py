from tkinter import *

def miles_to_km():
    miles=float(miles_input.get())
    km=round(miles*1.609)
    kilomters_result_label.config(text=f"{km}")

window=Tk()
window.title("Mile to kilometer converter")
window.config(padx=200,pady=200,bg="blue")

miles_input=Entry(width=20,bg="white")
miles_input.grid(column=1,row=0)


miles_label=Label(text="Miles",bg="white")
miles_label.grid(column=2,row=0)

is_equal_label=Label(text="is equal to",bg="white")
is_equal_label.grid(column=0,row=1)

kilomters_result_label=Label(text="0",bg="white")
kilomters_result_label.grid(column=1,row=1)

kilometer_label=Label(text="Km",bg="white")
kilometer_label.grid(column=2,row=1)

calculate_button=Button(width=20,text="Calculate",bg="white",command=miles_to_km)
calculate_button.grid(column=1,row=2 )

window.mainloop()

