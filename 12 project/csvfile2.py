import csv
def records(filename):
    f=open(filename,"r")
    csvr=csv.reader(f)
    for i in csvr:
        if int(i[2])<15:
            print(i)
name=input("Enter the name of file with proper extension:")
print("The records for stays which are under 15 days are as follows:")
records(name)
