from tkinter import *

window=Tk()
window.title("My first GUI program")
window.minsize(width=500,height=400)

#Label

my_label=Label(text=" I am a Label",font=("Arial",34,"bold"))
my_label.pack()

my_label["text"]="New text"
my_label.config(text="New text")

#Button

def button_clicked():
    print("my name us naurangi lal")
    new_text= input.get()
    my_label.config(text=new_text)
button=Button(text="Click me",command=button_clicked)
button.pack()


#Entry label
input=Entry(width=10)
input.pack()
print(input.get())

#text
text=Text(height=5,width=30)
#For cursors in textbox
text.focus()

#Adds some text to bedin with
text.insert(END,"Example of Multi-line text entry.")

#gets current value in text box at line 1 entry label
print(text.get("1.0"))
text.pack()

#Spinbox

def spinbox_used():

    #gets the current value inn spinbox
    print(spinbox.get())
spinbox=Spinbox(from_=0,to=10,width=5,command=spinbox_used)
spinbox.pack()
#Scale
#called  with current scale value
def scale_used():
    print(value)
scale=Scale(from_=0,to=100,command=scale_used)
scale.pack()

#Checkbutton

def checkbutton_used():
    #prints 1 if on button checked,otherwise 0.
    print(checked_status.get())
    #variable to hold on the checked state, 0 is off ,1 is on.
checked_status=IntVar()
checkbutton=Checkbutton(text="Is On?",variable=checked_status,command=checkbutton_used)
checked_status.get()
checkbutton.pack()

#Radiobutton

def ratio_used():
    print(ratio_state.get())
    #Variable to hold on to which ratio button value is checked
ratio_state=IntVar()
ratiobutton1=Radiobutton(text="Option1",value=1,variable=ratio_state,command=ratio_used)

ratiobutton2=Radiobutton(text="Option2",value=2,variable=ratio_state,command=ratio_used)
ratiobutton1.pack()
ratiobutton2.pack()

#lists
def listbox_used(event):
    #gets current selection from listbox
    print(listbox.get(listbox.curselection()))
listbox=Listbox(height=5)
fruits=["Banana","Cherry","Apple","Orange","Mango"]
for item in fruits:
    listbox.insert(fruits.index(item),item)
listbox.bind("<<ListboxSelect>>",listbox_used)
listbox.pack()
window.mainloop()
