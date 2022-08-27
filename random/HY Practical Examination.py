#Write a menu driven program to do the following:
#a. Display the initials of the name. 
#For eg:
#Input : Mohandas Karamchand Gandhi
#Output : M.K. Gandhi
#b. Check whether a number has odd number or even number of digits
#(without using similar pre-defined functions)

choice=int(input("To print the initials of a name, enter 1 \nTo check whether a number has odd number or even number of digits, enter 2\n"))
if choice==1:
    name=input("Enter a name:")
    l=name.split()
    space=""
    ln=""
    for i in range(len(l)-1):
       fn=l[i]
       ln=ln+fn[0].upper()+". "
    ln=ln+l[-1].upper()
    print(ln)
if choice==2:
    n=int(input("Enter a number:"))
    copy=n
    c=0
    while n!=0:
        c+=1
        n=n//10
    if (c%2==0):
        print("Even number of digits")
    else:
        print("Odd number of digits")
