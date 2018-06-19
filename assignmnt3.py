# 1. create the list with user defined input
x=input("enter the number")
y=input("enter the number")
z=input("enter the number")
w=input("enter the number")
list=[x,y,z,w]
print(list)


#2.Add the following list to the above created list
#("goggle","apple","facebook","microsoft","tesla")
list2=['google','apple','facebook','microsoft','tesla']
print(list.extend(list2))
print(list)




# 3. create the list with numbers and sort it in ascending order
list=[3,5,8,2,9]
print(list.sort())
print(list) #by default list is sorted in ascending order


#4.WAP to merge them into a single sorted array that contains every item from array A and B in ascending order
A=[4,8,2,5]
print(A.sort())
print(A)
B=[2,6,5,1,]
print(B.sort())
print(B)
C=(A+B)
print(C.sort())
print(C)



#5. count the numbers of times object occur.
list=[2,3,6,7,9,7,4,7,9,7,3,6,7]
print(list.count(7))


#6. count even and odd in a list.
n=int(input("enter a number:"))
if n%2==0:
   print("n is even")
else:
   print("n is odd") 

#7. implement stack and queue using list.
#for stack
list=[1,2,3,4]
print(list.pop())
#for queue
list=[1,2,3,4]
print(list)
list.reverse()
print(list)
print(list.pop())   











