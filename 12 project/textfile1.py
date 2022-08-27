f=open("poem.txt","r")
lines=f.read()
print("The words containing numbers are:")
for i in lines.split():
    print(i)
