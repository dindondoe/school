math=float(input("Enter the marks obtained in mathematics: "))
eng=float(input("Enter the marks obtained in english: "))
science=float(input("Enter the marks obtained in science: "))
if (eng+math+science)/3>=80:
     print("Pure Science")
elif (eng+science)/2>=90 and maths>=60:
     print("Bio. Science")
elif (eng+math+science)/3>=60:
     print("Commmerce") 
