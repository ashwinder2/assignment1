    #ASSIGNMENT-8
#Q1. what is time tuple.
#ans: We represent time in a way that’s easy for us to understand.
 # However, Python stores it in tuples.
 
# Index	Field	Domain of Values
# 0	Year   (4 digits)	Ex.- 1995
# 1	Month	1 to 12
# 2	Day  	1 to 31
# 3	Hour	0 to 23
# 4	Minute	0 to 59
# 5	Second	0 to 61 (60/61 are leap seconds)
# 6	Day of Week	 0 to 6 (Monday to Sunday)
# 7	Day of Year	 1 to 366 (Julian day)
# 8	DST     	-1,0,1


#Q.2- Write a program to get formatted time.
import time
print(time.asctime(time.localtime(time.time())))

 #Q.3- Extract month from the time.
 #extracting month
 import datetime
print(datetime.datetime.now().strftime('%m'))

 
 
 #Q.4- Extract day from the time.
 import datetime
print(datetime.date.today())
s=datetime.date.today()
print(s.day)



 #Q.5- EXTRACT date from the time.
 import datetime
print(datetime.date.today())
s=datetime.date.today()
print(s.day)

 # Q.6- Write a program to print time using localtime method.
import time
print(time.localtime(0)) 
 
 
# Q.7- Find the factorial of a number input by user using math package functions.
import math
print(math.factorial(int(input("enter any number: "))))


# Q.8- Find the GCD of a number input by user using math package functions.
x=int(input("enter number"))
y=int(input("enter other number"))
import math
print(math.gcd(x,y))

 # Q.9- Use OS package and do the following tasks: 
# 1. Get current working directory.
import os
print(os.getcwd)

# 2. Get the user environment.
import os
print(os.environ) 