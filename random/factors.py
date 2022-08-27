n=int(input("Enter a number "))
for i in range(1, n+1):
    if n%i==0:
        if(i%2==1):
            print(i)
