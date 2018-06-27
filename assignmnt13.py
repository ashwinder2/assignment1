                #ASSIGNMENT-13 (EXCEPTIONS AND HANDLING IN PYTHON)

# Q.1- Name and handle the exception occured in the following program: 

# a=3
 # if a<4:
    # a=a/(a-3)
     # print(a)
#solution: (zero division error) 
try:
    a=3
    if a<4:
      a=a/(a-3)
      print(a)
except Exception:
    print("Exception occured")
	
	
# Q.2- Name and handle the exception occurred in the following program: 
# l=[1,2,3]
# print(l[3])
#solution: (index error)
try:
   l=[1,2,3]
   print(l[3])
except Exception:
    print("Exception occured")
	
	
	
	
# Q.3- What will be the output of the following code:
#Program to depict Raising Exception

# try:
    # raise NameError("Hi there")  # Raise Error
# except NameError:
    # print "An exception"
    # raise  # To determine whether the exception was raised or not
	
#solution:
#Here the mistake is in the print statement which is given as :
#print("An exception")
#the code is written as-:
try:
   raise NameError("Hi there")  # Raise Error
except Exception:
    print("An exception")
    raise
#output: The output of the above code will simply line printed as “An exception” but a Runtime error
# will also occur in the last due to raise statement in the last line.
 #So, the output on your command line will look like.
# An exception
# Traceback (most recent call last):
  # File "assignmnt13.py", line 38, in <module>
    # raise NameError("Hi there")  # Raise Error
#NameError: Hi there




# Q.4- What will be the output of the following code:

 #Function which returns a/bS
# def AbyB(a , b):
	# try:
		# c = ((a+b) / (a-b))
	# except ZeroDivisionError:
		# print "a/b result in 0"
	# else:
		# print c

#Driver program to test above function
# AbyB(2.0, 3.0)
# AbyB(3.0, 3.0)
#Function which returns a/bS
#solution:The code is written as-
def AbyB(a , b):
    try:
        c=((a+b) / (a-b))
    except ZeroDivisionError:
        print ("a/b result in 0")
    else:
        print (c)

# Driver program to test above function
AbyB(2.0, 3.0)
AbyB(3.0, 3.0)

#output: -5.0
        #a/b result in 0



# Q.5- Write a program to show and handle following exceptions: 
# 1. Import Error
 #solution: ImportError
#Raised when an import statement fails.
try:
    from _foo import *
#_foo import* is not a module,so there is import error.

#after handling
except ImportError:
    print("hello world")


# 2. index Error
#solution:IndexError
#Raised when an index is not found in a sequence.
l=[1,2,3]
print(l)
print(l[3])
# the output of above code is index error:list is out of range.
try:
    print("fourth element ",(l[3]))
except IndexError:
#after handling.
   print("IndexError.... three elements only in list")


# 3. value Error
number = int(input("Enter a number between 1 - 10: "))
#if user input is no. then there is no error but if str then ValueError is occur.
try:
    print("you entered number",number)
#after handling.
except ValueError:
     print ("Error.... numbers only")


# Q.6- Create a user-defined exception AgeTooSmallError() that warns the user when they have entered age less than 18. 
# The code must keep taking input till the user enters the appropriate age number(less than 18). 
class Error(Exception):
   """Base class for other exceptions"""
   pass
 
class AgeTooSmallError(Error):
   """Raised when the entered age is smaller than the actual one"""
   pass
 
class AgeTooLargeError(Error):
   """Raised when the entered age is larger than the actual one"""
   pass

age = 18
 
while True:
   try:
       num=int(input("Enter an age: "))
       if num < age:
           raise AgeTooSmallError
       elif num > age:
           raise AgeTooLargeError
       break
   except AgeTooSmallError:
       print("incorrect")
   except AgeTooLargeError:
       print("The entered age is greater than 18")
print("correct")













