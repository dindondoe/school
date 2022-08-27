import pickle
import os
def Filter_book(author):
    f1=open("Book.dat","rb")
    f2=open("Book_new.dat","wb")
    try:
        while True:
            l=pickle.load(f1)
            if l[2]==author:#checks for equality
                pickle.dump(l,f2)#writes the value to the Book_new
    except EOFError:
        f1.close()
        f2.close()
auth=input("Enter the name of the author:")
Filter_book(auth)
f=open("Book_new.dat","rb")
print("The contents of the new file are:")
try:
    while True:
        k=pickle.load(f)
        print(k)
except EOFError:
    f.close()
os.remove("Book.dat")#deletes the original file

        
    
