a=int(input('Enter the length of the first side'))
b=int(input('Enter the length of the second side'))
c=int(input('Enter the length of the third side'))
if a+b>c and b+c>a and a+c>b:
      print("the triangle is valid")
else:
      print("the triangle is invalid")
