from tkinter import *



def button_clicked():
    print("Button got clicked")
    new_text= input.get()
    my_label.config(text=new_text)


window=Tk()
window.title("My first GUI program")
window.minsize(width=500,height=400)
window.config(padx=200,pady=20)
#Label
my_label=Label(text=" I am a Label",font=("Arial",20,"bold"))
my_label.config(text="New text")
#my_label.place(x=0,y=0)
my_label.grid(column=0,row=0)
#Button
button1=Button(text="Click me",command=button_clicked)
#button.place(x=125,y=10)
button2=Button(text="Click me",command=button_clicked)
button2.grid(column=3,row=0)
button1.grid(column=1,row=0)
#Entry label
input=Entry(width=10)
print(input.get())
#input.place(x=190,y=10)
input.grid(column=2,row=0)
window.mainloop()