def MagicN(list1):
   print("The magic numbers are:")
   for i in list1:
      copy=i
      s=0#resets every iteration
      while (i>0 or s>9):
         if (i==0):
            i=s
            s=0
         s+=i%10#sum of digits
         i=i//10
      if s==1:
         print(copy)
L1=eval(input("Enter a list:"))
MagicN(L1)
