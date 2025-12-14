# Create a new file “practice.txt” using python. Add the following data in it: 
# Hi everyone
# we are learning File I/O
# using Java. 
# I like programming in Java.

with open("practice.txt",'w') as f:
    f.write("Hi everyone \nwe are learning File I/O \nusing Java. \nI like programming in Java.")


# WAF that replace all occurrences of “java” with “python” in above file.

with open("practice.txt",'r') as f:
    data = f.read()
    print(data)
data=data.replace("Java", "python")
with open("practice.txt",'w') as f:
    f.write(data)


# Search if the word “learning” exists in the file or not. 

with open("practice.txt",'r') as f:
    data = f.read()
    if(data.count("learning") == 0):
        print("Word not found")
    else : print("word found")
    