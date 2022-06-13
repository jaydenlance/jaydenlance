#!/usr/bin/python

######################
#   Assignment: Designing a digital clock
#   Name    : Lance Jayden
#   Date    : 10 /06 /2022
######################

from tkinter import *
from time import strftime
root = Tk()
root.geometry("500x500")
root.resizable(0,0)
root.title('Python Clock')
Label(root,text = 'Lancerlot', font ='Gadugi 20 bold').pack(side=TOP)
def time():
    string = strftime('%H:%M:%S %p')
    mark.config(text = string)
    mark.after(1000, time)
mark = Label(root, 
            font = ('calibri', 40, 'bold'),
            pady=150,
            foreground = 'Black')
mark.pack(anchor = 'center')
time()

mainloop()