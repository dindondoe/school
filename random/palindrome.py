n=int(input("Enter a number: "))
r=0
copy=n
while n!=0:
    d=n%10
    r=r*10+d
    n=n//10
if r==copy:
    print("The number is a Palindrome")
else:
    print("The number is not a Palindrome")
