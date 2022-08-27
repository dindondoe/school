L1=[]
n=int(input("How many employees? "))
for a in range(n):
    r=int(input("Enter ID No."))
    L1.append(r)
    S=dict.fromkeys(L1, 45000)
    print(S)
