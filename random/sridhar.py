import math
sign1="+"
sign2="+"
a=float(input("Enter a:"))
b=float(input("Enter b:"))
c=float(input("Enter c:"))
D=(b*b)-(4*a*c)
x1=((-b)+math.sqrt(D))/(2*a)
x2=((-b)-math.sqrt(D))/(2*a)
if x1>0:
    sign1="-"
else:
    x1=(-1)*x1
if x2>0:
    sign2="-"
else:
    x2=(-1)*x2
print("( x",sign1,x1,")(x",sign2,x2,")")
