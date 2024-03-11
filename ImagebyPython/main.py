from PIL import Image
import numpy as np

class Canvas:
    def __int__(self,height,width,color):
        self.color=color
        self.height=height
        self.width=width
        self.data=np.zeros((self.height,self.width,3),dtype=np.uint8)
        self.data[:]=self.color

    def make(self,imagepath):
        img=Image.fromarray(self.data,'RGB')
        img.save(imagepath)

class Rectangle:
    def __int__(self,x,y,height,width,color):
        self.x=x
        self.y=y
        self.height=height
        self.width=width
        self.color=color

    def draw(self,canvas):
        canvas.data[self.x:self.y+self.height,self.y:self.y+self.width]=self.color

class Square:

    def __init__(self,x,y,side,color):
        self.color=color
        self.x=x
        self.y=y
        self.side=side

    def draw(self,canvas):
        canvas.data[self.x:self.x+self.side,self.y:self.y+self.side]=self.color

canvas=Canvas(height=20,width=30,color=(255,234,200))
r1=Rectangle(x=1,y=6,height=7,width=10,color=(250,100,170))
r1.draw(canvas)
s1=Square(x=1,y=3,side=3,color=(2,100,222))
s1.draw(canvas)
canvas.make('canvas.png')


