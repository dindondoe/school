t1=eval(input("Enter the first tuple:"))
t2=eval(input("Enter the second tuple:"))
l2=list(t2)#to allow mutation
for i in t2:
   if i in t1:#checks for presence
     l2.remove(i)
print("The changed  tuple is", tuple(l2))
