a=int(input("Enter the first angle of the triangle"))
b=int(input("Enter the second angle of the triangle"))
c=int(input("Enter the third angle of the triangle"))
if a+b+c==180:
    print("The triangle exists")
    if a!=b or b!=c or a!=c:
       print("The triangle is scalene")
    elif a==b!=c or b==c!=a or a==c!=b:
       print("the triangle is isosceles")
    elif a==90 or b==90 or c==90:
       print("The triangle is a right angled triangle")
else:
    print("The triangle does not exist")
