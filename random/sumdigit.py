n=int(input("Enter a number: "))
c=0
while n!=0:
    d=n%10
    c=c+d
    n=n//10
print("Sum of digits ",c)
