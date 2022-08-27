n=0
c=0
m=0
L1=[]
for i in range (10):
    n=int(input("Enter a number: "))
    L1.append(n)
t1=tuple(L1)
for j in t1:
    for k in range (1, j+1):
        if j%k==0:
            c+=1
    if c==2:
        m+=1
        print(j,"is a prime number")
    c=0
print("There are",m,"prime numbers")
   
