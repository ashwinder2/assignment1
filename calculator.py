
name=input("Hey, whats your name?\n")
print(name,"****** ","welcome to our mathematical calculations program","******")

import time
time.sleep(2)


# This function adds two numbers 
def add(x, y):
   return x + y

# This function subtracts two numbers 
def subtract(x, y):
   return x - y

# This function multiplies two numbers
def multiply(x, y):
   return x * y

# This function divides two numbers
def divide(x, y):
   return x / y
   
def raisetopower(x,y):
   return x**y

def floordivision(x,y):
   return x//y   

print()   

print("Please select the operation....which you want to perform: ")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Raise to power")
print("6.Floor division")
print()

# Take input from the user 
choice = input("Enter your choice(1/2/3/4/5/6):")

n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))

if choice == '1':
   print(num1,"+",num2,"=", add(num1,num2))

elif choice == '2':
   print(num1,"-",num2,"=", subtract(num1,num2))

elif choice == '3':
   print(num1,"*",num2,"=", multiply(num1,num2))

elif choice == '4':
   print(num1,"/",num2,"=", divide(num1,num2))
   
elif choice == '5':
   print(n1,"**",n2,"=", raisetopower(n1,n2))

elif choice == '6':
   print(n1,"//",n2,"=", floordivision(n1,n2)) 
   
else:
   print("Invalid input")