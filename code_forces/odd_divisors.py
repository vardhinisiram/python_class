import time


def check_odd(n):
    print(n)
    if n == 2:
        return "NO"
    elif n % 2 != 0:
        return "YES"
    else:
        return check_odd(n/2)

# 10529998476
if __name__ == "__main__":
    t = int(input())
    while t > 0:
        n = int(input())
        start = time.perf_counter()
        if n% 2 != 0:
            print("YES")
        else:
            print(check_odd(n))
        end = time.perf_counter()
        print(end - start)
        t-=1


"""

n=int(input())
start = time.perf_counter()
if n%2!=0:
    print("yes")
else:
    flag = False
    for i in range(3, n, 2):
        print(i)
        if n % i == 0:
            flag = True
if flag:
    print("YES")
else:
    print("NO")
end = time.perf_counter()
print(end - start)
"""
