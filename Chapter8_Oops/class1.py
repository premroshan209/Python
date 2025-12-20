#creating classes

class Stuent:
    name = "Vishal"

    def __init__(self, name = "Annonymous", marks = 0):
        self.name = name
        self.marks = marks
        print("Adding new student", name,"in database.")

    @staticmethod                                #Creating static method , it does not need any atributes
    def School():
        print("School Name : JNV Latehar")
    

#creating objects
S1 = Stuent("Yash",15)
S1.School()       #Calling static method using object name
Stuent.School()   #Calling static method using class name
S2 = Stuent()

S1.name = "Dhurandhar"
print(S1.name)
print(S1.marks)
print(S2.name)
print(S2.marks)
S3 = Stuent("Raj")
print(S3.name)
print(S3.marks)