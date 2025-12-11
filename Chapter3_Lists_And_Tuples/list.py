list = []

list.append(input("Enter 1st movie name: "))
list.append(input("Enter 2nd movie name: "))
list.append(input("Enter 3rd movie name: "))

print(list)

list.sort()
print(list)

list.sort(reverse=True)
print(list)

list.insert(0,"Salar")
print(list)

list.remove("Salar")
print(list)

list.pop(1)
print(list)