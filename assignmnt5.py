                                        # ASSIGNMENT 5
#take an input year from user and decide whether it is leap year or not.
year=int(input("enter the year: "))
if ((year%400==0)or((year%4==0)and(year%100!=0))):
  print("%d is a leap year" %year)
else:
  print("%d is not leap year" %year)  


#take length and breadth input from user and check whether the dimensions are of square or rectangle.
x=int(input("enter the length: ")) 
y=int(input("enter the breadth: "))
if x==y:
   print("it is a square") 
else:
   print("it is a rectangle")   

   
#Take the input age of 3 peoples and determine oldest and youngest among them.
x=int(input("enter the age of first people: "))   
y=int(input("enter the age of second people: "))  
z=int(input("enter the age of third people: "))
#for oldest  
if x>=y and x>=z:
   print("x is oldest")
elif y>=x and y>=z:
   print("y is oldest")
elif z>=x and z>=y:
   print("z is oldest")
else:
   print("all are same age")   
 #for youngest
if x<=y and x<=z:
   print("x is youngest")
elif y<=x and y<=z:
   print("y is youngest")
elif z<=x and z<=y:
   print("z is youngest")
else:
   print("all are same age")
   
   
#write am if statement to lets competitor..........should state"sorry no prize this time".
n=int(input("enter number of scored: "))
if n<=50:
 print("no prize")
elif n<=150:
 print("WOODEN PRIZE") 
elif n<=180:
 print("BOOK")
else:
 print("CHOCOLATES") 
 
 

#a shop will give discount of 10% if the cost of purchased quantity is more than 1000. ask user for___user.
qty=int(input("enter the quantity: "))
totalexp=qty*100
if totalexp>1000:
 dis=totalexp*0.10
 totalexp=totalexp-dis
 print("cost is %d" %totalexp)
else:
 print("total cost is %d" %totalexp) 






