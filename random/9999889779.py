n=int(input("Enter the value of n: "))
a=9
sum=0
for i in range(1,n+1):
    if i%2==1:
        print(a)
        sum+=a
    else:
        print(a*10+9)
        sum+=a*10+9
        a=a-1
print("The sum is: ",sum)
