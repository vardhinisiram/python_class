
"""
def fact(n):
    if n == 1:
        return 1
    else:
        val = n*fact(n-1)
        print("calling recursion with ",n, val)
        return val
"""

def even(n):
    if n == 0:
        return n
    else:
        if n % 2 == 0:
            print(n)
        return even(n-1)

print(even(10))
#print(fact(5))