# Write a recursive function to calculate the sum of first n natural numbers. 

def sum_n_no(n):
    if(n==1) : return 1
    return n + sum_n_no(n-1)

print(sum_n_no(5))


# Write a recursive function to print all elements in a list.
# Hint : use list & index as parameters. 

def print_list(list, i):
    if i == len(list) : return
    print(list[i],end=" ")
    print_list(list, i+1)

list = [1,2,3,4,5,6,7,8,9]
print_list(list,0)
print()
