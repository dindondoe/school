import pickle
f=open("Book.dat","rb")
def counting(price):
    count=0
    try:
        while True:
            l=pickle.load(f)
            if l[3]>price:#checks if price is greater
                count+=1#increases count by one for each book
    except EOFError:
        print("There are",count,"records of books which cost more than",price)
prc=int(input("Enter the price to compare to:"))
counting(prc)
