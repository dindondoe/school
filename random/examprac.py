s=input("Enter starting time:")
e=input("Enter ending time:")
fm=int(s[0:2])*60+int(s[2:])
em=int(e[0:2])*60+int(e[2:])
diffTime=em-fm
hrs=diffTime//60
mins=diffTime%60
print("The difference is",hrs,"hours,",mins,"minutes")
