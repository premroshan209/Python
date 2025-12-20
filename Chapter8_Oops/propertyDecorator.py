# property Decorator
# ~~~~~~~~~~~~~~~~~~
# we use @property decorator on any method in the class to use the method as a property

class Student:
    def __init__(self,phy,che,math):
        self.phy = phy
        self.che = che
        self.math = math
    @property
    def percentage(self):
        return str((self.phy + self.che + self.math) / 3) + "%"
    
stu = Student(80,90,98)
print(stu.percentage)