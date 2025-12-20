
# Inheritance
# ~~~~~~~~~~~
# when one class (child/derived) derives the properties and methods of another class (parent/base).
# Types |-> Single Inheritance
#       |-> Multi-level Inheritance
#       |-> Multiple Inheritance

class Car:
    classVar = "ABC"
    @staticmethod # Static method : it can't access or modify class state and generally for utility.
    def start():
        print("Car started..")
    @staticmethod
    def stop():
        print("Car stopped..")

    def change_classVar(self):
        self.__class__.classVar = "ABC" #or   Car.classVar = "ABC"
    
    @classmethod #or by using class method : a class method is bound to the class and receives the class as an implicit first argument
    def change_classVar_Using_classMethod(cls,name):  # cls just like self but not self and that refrs class
        cls.classVar = name

class ToyotaCar(Car):
    def __init__(self,brand):
        super().__init__()               # using super() keyword to initialise parent attributes 
        self.brand = brand

class Fortuner(ToyotaCar):
    def __init__(self, brand,type):
        super().__init__(brand)
        self.type = type
        super().start() #to acces parent methods

car1 = Fortuner("Fortuner","diesel")
car1.start()




# Multiple Inheritance
# ~~~~~~~~~~~~~~~~~~~~~

class A:
    varA = "Welcome to Class A"
    varD = "by class A"
class B:
    varB = "Welcome to Class B"
    varD = "by class B"
class C(A,B):
    varC = "Welcome to Class C"

var = C()
print(var.varA)
print(var.varB)
print(var.varC)
                                             # ---->
print(var.varD)  # prints "by class A because C(A,B)" priority is left to right