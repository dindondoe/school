import pickle
f=open("Student.dat","wb")
n=int(input("How many records do you wish to enter? "))
for i in range(n):
    rno=int(input("Enter the roll number:"))
    name=input("Enter the name of the student:")
    marks=float(input("Enter the marks obtained:"))
    l=[rno,name,marks]
    pickle.dump(l,f)#writes each record to file
print("File made successfully")
f.close()
f=open("Student.dat","rb")
print("The contents of the file are:")
try:
    while True:
        k=pickle.load(f)
        print(k)
except EOFError:
    print("End of file reached")



