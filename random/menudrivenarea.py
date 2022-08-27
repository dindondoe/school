choice=int(input("Press 1 to find area of circle \nPress 2 to find area of square\nPress 3 to find area of rectangle\n"))
if choice==1:
    r=float(input("Enter the radius of the circle "))
    ar1=(3.14)*r*r
    print("The area of the circle is ",ar1)
elif choice==2:
    s=float(input("Enter the side of the square "))
    ar2=s*s
    print("The area of the square is ",ar2)
elif choice==3:
    l=float(input("Enter the length of the rectangle "))
    b=float(input("Enter the breadth of the rectangle "))
    ar3=l*b
    print("The area of the rectangle is ",ar3)
