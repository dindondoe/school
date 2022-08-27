n=int(input("Enter a number:"))
s=0
f=1
copy=n
while n!=0:
    d=n%10
    for i in range(1,d+1):
        f=f*i
    s+=f
    f=1
    n=n//10
if s==copy:
    print("The number is a special number")
else:
    print("The number is not a special number")
