n=int(input("Enter the value of n: "))
l1=[0]
x = 0
y = 1
z=x+y
mid=0
for i in range (1,n):
    l1.append(z)
    z=x+y
    x=y
    y=z
print(l1)
if n%2!=0:
    mid=((n+1)//2)-1
else:
    mid=n//2
print(l1[mid])
