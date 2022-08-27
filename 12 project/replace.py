def Replc(str1,chr1,chr2):
    L=list(str1)
    ind=0#stores index value 
    for i in L:
        if i==chr1
           L[ind]=chr2
        ind+=1
    return "".join(L)#changes the list back into a word
s=input("Enter a string:")
rem=input("Enter character to be removed:")
rep=input("Enter character to replace it with:")
print("The modified word is", Replc(s,rem,rep))
