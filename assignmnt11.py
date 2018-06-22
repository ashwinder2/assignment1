                                             #ASSIGNMENT-11  (THREADS)

#Q1. Create a threading process such that it sleeps for 5 seconds and then prints out a message
import threading
from threading import Thread
import time
def display():
    for x in range(10):
        print(threading.current_thread().getName(),"hello world")
        time.sleep(5)
t=Thread(target=display)
t.start()

#Q2. Make a thread that prints numbers from 1-10, waits for 1 sec between.
import threading
from threading import Thread
import time
def display():
    for x in range(10):
        time.sleep(1)
        print("the thread is",x)
       
t=Thread(target=display)
t.start()

# Q3. Make a list that has 5 elements.
# Create a threading process that prints the 5 elements of the list with a delay of multiple of 2 sec between each display.
# Delay goes like 2sec-4sec-6sec-8sec-10sec
x=int(input("enter the no."))
y=int(input("enter the no."))
z=int(input("enter the no."))
w=int(input("enter the no."))
v=int(input("enter the no."))
l=[x,y,z,w,v]
print(l)
import threading
from threading import Thread
import time
def display(n):
    d=2   
    for l in n:
         time.sleep(d)
         d=d+2
         print("the thread is ",l)
t=Thread(target=display,args=(l,))
t.start()
 



#Q.4 call a factorial function using threads.
import threading
from threading import Thread
import time
import math

def display():
    x=int(input("enter the no. :"))
    a=math.factorial(x)
    print("result: ",a)


t=Thread(target=display)
t.start()
    






