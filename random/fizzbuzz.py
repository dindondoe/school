N=int(input("Enter number:"))

if N%5==0 and N%7==0:
 print("FIZZBUZZ")
elif N % 5==0:
 print("BIZZ")
elif N % 7==0:
 print("FIZZ")
else:
    print("Not divisible by either")
