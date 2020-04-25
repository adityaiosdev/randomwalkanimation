from tkinter import*
import numpy as np
from random import random
import time

width = 800
height = 600

tk=Tk()
canvas = Canvas(tk,width=width,height=height)
tk.title("Random Walk 2D") 
canvas.pack()
    
class Ball:
    def __init__(self,color,size):
        self.shape = canvas.create_oval(5,5,30,30,fill="orange")
        self.x= random()
        self.y=random()
    def move(self):
        rand= random()
        if(rand<=0.25):
            self.x = self.x + 1
        #down
        elif(rand<=0.50):   
            self.y = self.y - 1
        #left
        elif(rand<=0.75):
            self.x = self.x - 1
        #up
        else:
            self.y = self.y + 1
        #if (self.x>height):
         #   self.x = self.x - height
        #if (self.x<0):
         #   self.x = self.x + height
        #if (self.y>width):
         #   self.y = self.y - width
        #if (self.y<0):
         #   self.y = self.y + width
        
        canvas.move(self.shape,self.x,self.y)
        pos = canvas.coords(self.shape)
        if pos[3]>=height or pos[1] <= 0:
            self.y=-self.y
        if pos[2]>=width or pos[0]<=0 :
            self.x=-self.x

balls = []
for i in range (100):
    balls.append(Ball("red",50))

while True:
    for ball in balls:
        ball.move() 
    tk.update()
    time.sleep(0.3)
tk.mainloop()
