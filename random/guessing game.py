import random
n=random.randint(1,100)
c=1
a=int(input("Enter your guess:"))
while a!=n:
    if a>n:
        print("Too high!")
    else:
        print("Too low!")
    a=int(input("Guess again!:"))
    c+=1
else:
    print("Correct!",end="")
    print("You took ",c,"tries to get it right!")
