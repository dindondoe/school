import csv
f=open("travel_company2.csv","w+",newline='')
csvw=csv.writer(f,delimiter='\t')
n=int(input("How many records do you wish to enter? "))
for i in range(n):
    idno=input("Enter the ID number:")
    dest=input("Enter the destination:")
    days=input("Enter how long the stay is (in days):")
    fare=input("Enter the total fare:")
    l=[idno,dest,days,fare]
    csvw.writerow(l)#writes list to file
print("File successfully made")
f.close()
f=open("travel_company2.csv","r")
csvr=csv.reader(f,delimiter='\t')
print("The contents of the file are:")
for line in csvr:
    print(line)#prints each line of the csv file
f.close()


