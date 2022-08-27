D1={}
l1=[]
a=0
b=0
maxx=None
minn=None 
for i in range(1,8):
    day=(input("What day of the week? "))
    for k in range(0,1):
        a=int(input("Enter the maximum temperature: "))
        l1.append(a)
        b=int(input("Enter the minumum temperature: "))
        l1.append(b)
        minn=b
        tup1=tuple(l1)
        if a>maxx:
            maxx=a
        if b<minn:
            minn=b
    l1=[]
    D1[day]=tup1
print("The highest temperature is ",maxx)
print("The lowest temperature is ",minn)
