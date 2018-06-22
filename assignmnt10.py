# Q.1- Create a class Animal as a base class and define method animal_attribute.
# Create another class Tiger which is inheriting Animal and access the base class method.



# Q.2- What will be the output of following code.

class A:
 def f(self):
      return self.g()

 def g(self):
      return 'A'

class B(A):
 def g(self):
      return 'B'
a = A()
b = B()
print a.f(), b.f()
# Q.3- Create a class Cop. Initialize its name, age , work experience and designation.
 # Define methods to add, display and update the following details. Create another class Mission which extends the class Cop.
 # Define method add_mission _details. Select an object of Cop and access methods of base 
 # class to get information for a particular cop and make it available for mission.

# Q.4- Create a class Shape.Initialize it with length and breadth Create the method Area.
 # Create class rectangle and square which inherits shape and access the method Area.