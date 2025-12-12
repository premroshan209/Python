# WAP to find the factorial of first n numbers. (using for)
n = int(input("Enter n: "))
m = 1
for el in range(1,n+1):
    m *=  el
else:
    print("factorial : ", m)