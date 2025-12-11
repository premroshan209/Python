"""WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with
an empty dictionary & add one by one. Use subject name as key & marks as value."""

dist = {}

x = int(input("Enter marks of Math Subject : "))
dist.update({"Math":x})

x = int(input("Enter marks of Science Subject : "))
dist.update({"Science":x})

x = int(input("Enter marks of English Subject : "))
dist.update({"English":x})

print(dist)