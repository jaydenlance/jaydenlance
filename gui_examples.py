#!/usr/bin/python

###########################
#      gui__examples using ktinker
#      Name : Lance Jayden 
#      Date : 7/6/2021
###########################

from tkinter import *

window = Tk()
window.title("Welcome to Jaydens Awesome App")
window.configure(bg='dark blue')
window.geometry("400x400") #fix the window size
F_name = Label (window, text = "First Name",font=("Aerial Bold", 20))
S_name = Label (window, text = "Second Name",font=("Aerial Bold", 20))

F_name.grid(column = 60 , row=110)

S_name.grid(column = 60 , row = 120)

btn = Button(window,text = "Sign Up", bg = 'purple', fg = 'red')
btn.grid(column = 100, row =180 )

F_name_box = Entry(window , width = 20)
F_name_box.grid(column = 100 , row = 120)

S_name_box = Entry(window , width = 20)
S_name_box.grid(column = 100 , row = 110)

def open_popup():
    top = Toplevel(window)
    top.geometry("300x300")
    top.title("Pop Up Window")
    top.configure(bg = 'yellow')
    msg = Label(top,text = "Welcome to the Dimtiry app")

window.mainloop()


