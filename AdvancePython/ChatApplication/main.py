from tkinter import *
import random
from datetime import datetime as dt
import os


class Chat:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1450x700+0+0")
        self.root.title("Chat Application")

        self.user_Input=StringVar()
        self.greetIntent = ["hi", "hello", "hey", "hi there", "hello there", "hey there"]
        self.dateIntent = ["what's the date", "please tell me date", "date", "today's date"]
        self.timeIntent = ["what's the time", "please tell me time", "time", "current time"]
        self.songsIntent = ["play song", "music", "play music", "song"]


        F1=LabelFrame(self.root,labelanchor="n",text="Chat Application",font=('times new roman', 30, 'bold'),width=1240,height=620,bd=3)
        F1.place(x=10,y=0,width=800)

        # user=Label(F1,text="User")
        # user.grid(row=0,column=0)
    

        textArea = Label(F1,bd=0,relief=GROOVE)
        textArea.grid(row=0,column=1)
        scroll_y = Scrollbar(textArea, orient=VERTICAL)
        self.txtarea = Text(textArea, yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH, expand=1)


    def get(self):
            self.msg = input("Enter your message : ")
            self.msg = self.msg.lower()

    def greet_indent(self):
        self.get()
        if self.msg in self.greetIntent:
            self.ans = random.choice(self.greetIntent)

    def date_Indent(self):
        self.get()
        if self.msg in self.dateIntent:
            self.current_date = dt.now().date()
            self.current_date.strftime("%d %B, %Y, %A")

    def time_Indent(self):
        self.get()
        if self.msg in self.timeIntent:
            self.current_time = dt.now().time()
            self.current_time.strftime("%H:%M:%S, %p")

    def date_Indent(self):
        self.get()
        if self.msg in self.songsIntent:
            self.songs_dir = r"D:\music"
            self.songs_list = os.listdir(self.songs_dir)
            self.song = random.choice(self.songs_list)
            self.song_path = self.songs_dir + "/" + self.song
            os.startfile(self.song_path)

    def exit(self):
        self.get()
        if self.msg == "bye":
            self.root.destroy()






root=Tk()
obj=Chat(root)
root.mainloop()