           #ASSIGNMENT-9TH (CLASSES AND MODULES)

# Q.1- create a cirle class and initialize it with radius.
class circle():
 def __init__(self,radius):
  self.radius = radius
 def  getArea(self):
  return 3.14*self.radius*self.radius
 def getCircumference(self):
  return self.radius*2*3.14
r=int(input("enter radius of circles: "))
obj=circle(r)
print("area of circle:",round (obj.getArea(),2))
print("circumfrence of circle:",round (obj.getCircumference(),2))
				


# Q.2- Create a Student class and initialize it with name and roll number. Make methods to :
# 1. Display - It should display all informations of the student.
class Student():
 def __init__(self,name,roll):
    self.name = name
    self.roll= roll
 def display(self):
    print (self.name)
    print (self.roll)
s1=Student(12,"deep")
s1.display()


  

# Q.3- Create a Temprature class. Make two methods :
# 1. convertFahrenheit - It will take celsius and will print it into Fahrenheit.
class Temperature():
 print("celsius=37.5")
 print(" celsius to fahrenheit ")
celsius = 37.5
fahrenheit=(celsius*9/5)+32
print("fahrenheit:",fahrenheit)



   
# 2. convertCelsius - It will take Fahrenheit and will convert it into Celsius.
class Temperature():
 print("temperature")
 #get the fahrenheit
fahrenheit = float(input("enter temp in fahrenheit: "))
#convert fahrenheit to celsius
celsius = (fahrenheit - 32)*5/9
print("celsius:",celsius)


# **Q.4- Create a class MovieDetails and initialize it with Movie name, artistname,Year of release and ratings .
# Make methods to 
# 1. Display-Display the details.
class MovieDetails():
  def __init__(self,name,artistname,release,ratings):
    self.name = name
    self.artistname = artistname
    self.release = release
    self.ratings = ratings
  def display(self):
    print(self.name)  
    print(self.artistname)
    print(self.release)
    print(self.ratings)
m1=MovieDetails("pyar","abc",2017,5)
m1.display()

# Q.5- Create a class Expenditure and initialize it with expenditure,savings.Make the following methods. 
# 1. Display expenditure and savings 
class expenditure():
 def __init__(self,expenditure,savings):
    self.expenditure=expenditure
    self.savings=savings
 def display(self):
    print(self.expenditure) 
    print(self.savings)
e1=expenditure(15000,12000)
e1.display()
# Calculate total salary and display it.
expenditure=15000
savings=12000
salary=expenditure+savings
print("salary: ",salary)


	 