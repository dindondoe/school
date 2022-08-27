import pickle
def CreateFile():
    f=open("Book.dat","wb")
    n=int(input("How many records do you wish to enter? "))
    for i in range(n):
        BookNo=input("Enter the ID number of the book:")
        BookName=input("Enter the name of the book:")
        Author=input("Enter the author's name:")
        Price=float(input("Enter the price of the book:"))
        l=[BookNo,BookName,Author,Price]
        pickle.dump(l,f)#writes each record to file
    print("File made successfully")
    f.close()
CreateFile()
f=open("Book.dat","rb")
print("The contents of the file are:")
try:
    while True:
        k=pickle.load(f)
        print(k)
except EOFError:
    print("End of file reached")



