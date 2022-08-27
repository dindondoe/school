n=int(input("Enter the number of rows "))
for i in range(1, n+1):
    for j in range(1, i+1):
        if j==i:
            print(j, end="")
        else:
            print(end=" ")
    print("")
    
