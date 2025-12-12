# WAP to find the sum of first n numbers. (using while)
n = int(input("Enter n: "))
sum = 0
i = 0
while i <= n:
    sum+=i
    i+=1
print("Sum = ", sum)