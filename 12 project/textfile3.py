with open("source.txt") as f1,open("target.txt","w") as f2:#file object created
    lines=f1.readlines()
    for i in lines:
       if list(i[0])[0]!="T":#checks if first letter in first word is 'T'
            f2.write(i)
    print("Completed.")

