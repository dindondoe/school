l1=eval(input("Enter a list: "))
m=0
c=0
word=""
for i in l1:
    for j in i:
        if j not in "aeiouAEIOU":
            c+=1
    if c>m:
        m=c
        c=0
        word=i
print("Word with most consonants is "+word)
