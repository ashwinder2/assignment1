    #ASSIGNMENT 7
#1.create a function to calculate the area of a circle by taking radius from user.
def area():
 pi=3.14
 rad=float(input("enter the radius: "))
 area=(pi*rad*rad)
 print(area)
area()

#2.write a function "perfect" that determines if parameter number is a perfect number.
#use this function in a program that determine and print all the perfect numbers between 1 and 1000.
def perfect (n):
    sum=0
    for x in range(1,n):
        if n % x == 0:
            sum = sum + x
    if sum == n:
        print("perfect number: ",n)
for x in range (1,1001):
    perfect (x)		
	
#3. print multiplication table of 12 using recursion.
def table(n,i):
 print(n*i)
 i=i+1
 if i<=10:
  table(n,i)
table(12,1)

#4. write a function to calculate power of a number raised to other(a*b) using recursion.
def power (a,b):
 if b==1:
  return(a)
 if(b!=1):
  return(a*power(a,b-1))
a=int(input("enter the base: "))
b=int(input("enter exponential value: "))
print("result: ",power(a,b))


#5. write a function to find factorial of a number but also store the factorials calculated in a dictionary.
def factorial(n):
    if(n <= 1):
	    return 1
    else:
        return(n*factorial(n-1))
n=int(input("enter number: "))
print("factorial")
print(factorial(n))
c=factorial(n)
l="output"
d={}
d[l]=c
print(d)
print("\n")		













  