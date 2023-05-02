a = float(input("enter maths marks :"))
b = float(input("enter physics marks :"))
c = float(input("enter chemistry marks :"))
d = float(input("enter biology marks :"))
e = float(input("enter computer marks :"))
percentage = (a+b+c+d+e)/500*100
print("the percentage is ", percentage)
if percentage >= 90 :
    print("grade = A")
if percentage >= 80 and percentage < 90:
    print("grade = B")
if percentage >= 70 and percentage < 80:
    print("grade = C")
if percentage >= 60 and percentage < 70:
    print("grade = D")
if percentage >= 40 and percentage < 60:
    print("grade = E")
if percentage < 40 :
    print("grade = F")
