# rint the elements of the following list using a loop:

list = [1, 4, 9, 16, 25, 36, 49, 64, 81,100]

for el in list :
    print(el)

# Search for a number x in this tuple using loop:

n = int(input("Enter searching number: "))
for el in list:
    if(el == n):
        print({"Element found"})
        break
else :
    print("Element not found")