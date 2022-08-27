l1=eval(input("Enter a list:"))
a=int(input("Enter the number to remove:"))
c=l1.count(a)
while c>0:
    i=l1.index(a)
    l1.pop(i)
    c-=1
print("Modified list is ",l1)
