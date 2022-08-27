tup=eval(input("Enter a tuple:"))
if sorted(tup)==list(tup):
    print("It is sorted in ascending order")
else:
    print("It is not in ascending order\nIf sorted, the tuple is ",sorted(tup))
