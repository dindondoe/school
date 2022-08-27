#Write a program to generate
#all Niven numbers till 1000 in a list.
#Display the odd and even niven numbers as separate lists.
#[Hint: A niven number is divisible by the sum of its digits. Eg:156]

oddlist=[]
evenlist=[]
s=0
copy=0
d=0
for i in range(1, 1000):
    copy=i
    while copy>0:
        d=copy%10
        s+=d
        copy=copy//10
    if i%s==0 and i%2==0:
        evenlist.append(i)
    elif i%s==0 and i%2!=0:
        oddlist.append(i)
    s=0
print("The list of all the even Niven numbers is", evenlist)
print("The list of all the odd Niven numbers is", oddlist)

