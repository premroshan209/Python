# Polimorphism
# ~~~~~~~~~~~~
# when the same operator is allowed to have different meaning according to the context.

# D=Operators and  Dunder functions
#    a + b            ->              a.__add__(b)  
#    a - b            ->              a.__sub__(b)  
#    a * b            ->              a.__mul____(b)  
#    a / b            ->              a.__truediv____(b)  
#    a % b            ->              a.__mod____(b)  


# example : Predefined Polimorphism
print(1 + 2)              # 3
print("abc" + "def")      # concatenate
print([1,2,3] + [4,5,6])  # merge




# Complex number creation and addition
# Customised polinorphism of addition
class Complex:
    def __init__(self,i,j):  # i is real and j is imaginary
        self.i = i
        self.j = j
    
    def showNumber(self):
        print(self.i,"i +",self.j,"j")

    def __add__(self,num2):       # here we use Dunder functions 
        new_i = self.i + num2.i
        new_j = self.j + num2.j
        return Complex(new_i, new_j)
    
    def __sub__(self,num2):       # here we use Dunder functions 
        new_i = self.i - num2.i
        new_j = self.j - num2.j
        return Complex(new_i, new_j)

num1 = Complex(2,3)
num2 = Complex(5,7)
num3 = num1 + num2
num3.showNumber()
num4 = num1 - num2
num4.showNumber()
        