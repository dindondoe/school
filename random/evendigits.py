n=int(input("Enter a number: "))
unique=[]
print("The even digits are:")
while n!=0:
    d=n%10
    if d%2==0 and d not in unique:
        unique.append(d)
    n=n//10
    unique.reverse()
print("".join(str(num) for num in unique))
