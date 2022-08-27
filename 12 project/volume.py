def volume(l=4,b=4,h=4):
    k=l*b*h
    return k
a=int(input("Enter the length of the box:"))
b=int(input("Enter the breadth of the box:"))
c=int(input("Enter the height of the box:"))
print("The volume of the box is",volume(a,b,c),"cube units")
