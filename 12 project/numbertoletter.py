n=int(input("Enter a number: "))
L1=[]
s=" "#contains final output
D1={1:"One",2:"Two",3:"Three",4:"Four",5:"Five",6:"Six",7:"Seven",8:"Eight",9:"Nine",0:"Zero"}
while n>0:
    dig=n%10#digit extraction
    L1.append(D1[dig])
    n=n//10
L1.reverse()
print("The number in words is", s.join(L1))
