import csv
f=open("travel_company.csv","w+",newline='')
csvw=csv.writer(f)
n=int(input("How many records do you wish to enter? "))
for i in range(n):
    idno=int(input("Enter the ID number:"))
    dest=input("Enter the destination:")
    days=int(input("Enter how long the stay is (in days):"))
    fare=float(input("Enter the total fare:"))
    l=[idno,dest,days,fare]#holds value to be written to file
    csvw.writerow(l)#writes list to file
print("File successfully made")
f.close()
f=open("travel_company.csv","r")
csvr=csv.reader(f)
print("The contents of the file are:")
for line in csvr:
    print(line)#prints each line of the csv file

    
            
    
