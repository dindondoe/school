import pickle
def Update_book(idno):
    f=open("Book.dat","rb+")
    l=[]
    try:
        while True:
            pos=f.tell()#position to overwrite record
            l1=pickle.load(f)
            l=l1
            if int(l1[0])==idno:
                l[3]=float(input("Enter the new price:"))#new list created with changed value
            f.seek(pos)
            pickle.dump(l,f)#overwrites old record with the new one
    except EOFError:
        f.close()
search=int(input("Enter the ID of the book whose cost you want to change:"))
Update_book(search)
f=open("Book.dat","rb")
print("The contents of the file are:")
try:
    while True:
        l=pickle.load(f)
        print(l)
except EOFError:
    print("End of file")
    f.close()

        
