a = int(input())
b = int(input())

try:
    val = a/b
except ZeroDivisionError as e:
    print(e.__class__)
    print(e)
    val = "infinity"


print(val)