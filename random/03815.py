n=int(input("Enter the value of n: "))
d=1
sum=0
for i in range (1, n+1):
    d=i*i-1
    print(d)
    sum+=d
print("The sum is: ",sum)
