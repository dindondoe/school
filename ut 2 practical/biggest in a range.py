l = eval(input("Enter the list: "))
start = int(input("Enter start index: "))
stop = int(input("Enter stop index: "))
slice = l[start : stop]
mx=0
c=0
bw=""
for i in slice:
    c=len(i)
    if c>mx:
        m=c
        bw=i
print("The biggest word is ",bw," with ",m," letters")

