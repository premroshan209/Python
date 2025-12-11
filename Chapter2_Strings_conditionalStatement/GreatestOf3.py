a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

greatest = 0
if(a >= b and a >= c):
    greatest = a
elif(b >= c):
    greatest = b
else: 
    greatest = c

print("Greatest Number is : ", greatest)