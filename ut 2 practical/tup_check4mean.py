tup=(1,3,6,9,11,10)
s=0
l=len(tup)
for i in tup:
    s+=i
mean=s/l
if mean in tup:
    print("The mean is ",mean," and it is part of the tuple")
else:
    print("The mean is ",mean," and it is not present in the tuple")
