# Q1. Write a python program using tkinter interface to write Hello World and a exit button that closes the interface.
#solution:

# import tkinter
# from tkinter import *
 #import sys


# def display():
    # print("Hello World")
    # sys.exit()
# root = Tk()
# b= Button(root,text="EXIT",width=25, bg = 'red' ,fg= 'white', command= display)
# b.pack()
# root.mainloop()

# Q2. Write a python program to in the same interface as above and create a action when the button is click it will display
# some text.
#solution:
# import tkinter
# from tkinter import *



# def display():
    # print("Hello World")

# root = Tk()
# b= Button(root,text="Click",width=25, bg = 'blue' ,fg= 'white', command= display)
# b.pack()
# root.mainloop()


# Q3. Create a frame using tkinter with any label text and two buttons.
# One to exit and other to change the label to some other text.
#solution:
import tkinter 
from tkinter import *
import sys

def exit():
    sys.exit()

def display():
	label.config(text='chai pilo')

root = Tk()
root.geometry("250x250")

label=Label(root,text='Hello fraands')
label.pack()

f1=Frame(root)
f1.pack(side=TOP)

b1= Button(f1,text="EXIT",width=25, bg = 'red' ,fg= 'white', command=exit)
b1.pack()

b2= Button(f1,text="click",width=25, bg = 'red' ,fg= 'white', command= display)
b2.pack()

root.mainloop()


 
# Q4. Write a python program using tkinter interface to take an input in the GUI program and print it.
#solution:
# import tkinter
# from tkinter import *
# def show():
    # print(entry.get())

# root = Tk()
# entry=Entry(root,width=200)
# entry.pack()
# b=Button(root,text="click",width=20,bg='orange',fg='white',command=show)
# b.pack()
# root.mainloop()