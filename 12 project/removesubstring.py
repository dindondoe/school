s=input("Enter a sentence:")
q=input("Enter the substring to check for:")
l=len(q)
k=0#will store the no. of times it occurs
c=0#used to update index number for string slicing
if q in s:
    for i in s:
        x=s[c:l]
        l+=1
        c+=1
        if x==q:
            k+=1
    print("It occur s",k,"times")
else:
    print("The given substring is not present in the string")

            
