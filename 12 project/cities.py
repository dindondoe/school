def AFIND(CITIES):
    print("The following cities' names begin with an 'A'")
    for i in CITIES:
        if i[0]=="A":
            print(i)
l1=eval(input("Enter a list of cities: "))
AFIND(l1)
