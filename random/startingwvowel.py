n=input("Enter a sentence:")
n=n+' '
x=""
for i in n:
    if i!=' ':
        x=x+i
    else:
        if x[0] in "aeiouAEIOU"):
            print(x)
        x=""
