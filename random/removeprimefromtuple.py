t1=eval(input("Enter a tuple:"))
c=0
l1=list(t1)
for i in l1:
    for j in range(1,i+1):
        if i%j==0:
            c+=1
    if c==2:
        l1.remove(i)
    c=0
t1=tuple(l1)
print(t1)
