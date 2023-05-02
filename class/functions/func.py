"""
A function is a self contained block of statements written to execute a specific task.

"""


"""
def sum_2(a, b):
    print(a+b)
    return a + b

value = sum_2(10, 20)
print(value)
print(sum_2(15, 20))
"""

def even_numbers(integer = 10): # called function | function defnition.
    values = []
    i = 1 # initialisation...
    while i <= integer: # condition...
        if i % 2 == 0:
            values.append(i)
            #print(i, n, end = " * ", sep = " | ")
        i = i + 1 # updation......
    print()
    return values

def imp_func():
    print("Even odd imporant informaion")


if __name__ == "__main__":
    n = int(input("Enter the range"))
    evens = even_numbers(n)  # function call 
    print(evens)
    print(even_numbers())


