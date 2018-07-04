                                     #ASSIGNMENT-18 (GUI-2)
						
#Q1.Create a dict with name and mobile number.
#Define a GUI interface using tkinter and pack the label and create a scrollbar to scroll the list of keys in the dictionary.
#solution:
import tkinter
from tkinter import *

d={'deep': 8685811069,'ash': 1234567890, 'noor': 897654321}
root=Tk()
s=Scrollbar(root)
s.pack(side=RIGHT,fill=Y)
l=Listbox(root,yscrollcommand=s.set)
for line in d.values():
    l.insert(END,'this is the no'+str(line))
l.pack(side=LEFT,fill=BOTH)
s.config(command=l.yview())
root.mainloop()



#Q2.In the same tkinter file as created above, create a function to insert items into the dictionary.
import tkinter
from tkinter import *
d={'deep': 8685811069,'ash': 1234567890, 'noor': 897654321}
def insert():
    k=entry1.get()
    v=entry2.get()
    d[k]=v
    l.insert(END,k)
    print(d)
root=Tk()
entry1=Entry(root)
entry1.pack()
entry2=Entry(root)
entry2.pack()
b=Button(root,text="insert",command=insert)
b.pack()
s=Scrollbar(root)
s.pack(side=RIGHT,fill=Y)
l=Listbox(root,yscrollcommand=s.set)
for key in d.values():
    l.insert(END,'this is the list of no'+str(key))
l.pack(side=LEFT,fill=BOTH)
s.config(command=l.yview())
root.mainloop()
