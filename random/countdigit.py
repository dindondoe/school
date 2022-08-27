n=int(input("Enter a number: "))
c=0
while n!=0:
    d=n%10
    print(d)
    c+=1
    n=n//10
print("Number of digits are: ",c)
