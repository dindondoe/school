name=input("Enter a name: ")
L1=name.split()
ln=""
n=""
for i in range(len(L1)-1):
    n=L1[i].capitalize()
    print(n[0]+". ", end="")
print(L1[-1].capitalize())

    
               
