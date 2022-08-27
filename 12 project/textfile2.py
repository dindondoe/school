with open("nice.txt") as f:#file object created
    count=0 #stores how many times it occurs
    f1=f.read()
    for i in f1.split():
        if i.lower()=="the":
            count+=1
print("The word \"the\" occurs",count,"times")
