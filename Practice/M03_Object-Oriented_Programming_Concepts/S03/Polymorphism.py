class B:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __add__(self,val):
        return (self.x+val.x,self.y+val.y)
    def __sub__(self.x-val.x,self.y-val.y)
    pass 
a =B(10,20)
b =B(30,40)
print(a + b)
print(a - b)
#method overriding : same method in both parent and child class 
class Parent:
    def display(self):
        print("Parent class display method")
class Child(Parent):
    def display(self):
        print("Child class display method")
c = Child()
c.display()
Parent.display(c)
#Duck typing
class Dog:
    def sounds(self):
class Cat:
    def Sounds(self):
        print("Meow")
def make_sound(animal):
    animal.Sounds()
make_sound(Dog())
make_sound(Cat())


