L1=eval(input("Enter a list:")) 
c=0
print("The square numbers are:")
for i in L1:
    c=i**0.5#calculates root
    if c==int(c):#checks if the root is an integer
        print(i)
        
