# WAF to print the length of a list. ( list is the parameter)

def find_length(list):
    l = len(list)
    print(l)
    return l

list = [1,2,3,4,5,6,7,8,9]
find_length(list)

# WAF to print the elements of a list in a single line. ( list is the parameter)

def print_list(list):
    for el in list:
        print(el, end=" ")

list = [1,2,3,4,5,6,7,8,9]
print_list(list)
print()

# WAF to find the factorial of n. (n is the parameter)

def fact(n):
    m = 1
    for el in range(1,n+1):
        m*=el
    print(m)
    return m

fact(5)


# WAF to convert USD to INR. 

def usd_to_inr(usd):
    rs = usd * 90
    print(rs)
    return rs

usd_to_inr(10)