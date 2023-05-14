n=int(input())
a=" i hate that"
b=" i love that"
val = ""
if n==1:
    val = "i hate it"
elif n%2!=0:
    val="i hate that"+(n//2-1)*(b+a)+b+" i hate it"
else:
    val="i hate that"+(n//2-1)*(b+a)+" i love it"

print(val)
