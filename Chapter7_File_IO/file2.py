# WAF to find in which line of the file does the word “learning”occur first. 
# Print -1 if word not found. 

found = -1

def check_word_in_line():
    with open("practice.txt",'r') as f:
        line = 1
        word = "learning"
        for data in f:
            if word in data:
                print(line)
                return
            line += 1
    print(-1)
    return -1

check_word_in_line()


# From a file containing numbers separated by comma, print the count of even numbers.

with open("number.txt",'r') as f:
    data = f.read()
    list = data.split(sep=",")
    print(list)
even_count = 0
for el in list:
    if(int(el) % 2 == 0) : even_count += 1
print(even_count)