year = int(input("Enter a 4 digit year: "))  
if (year % 4) == 0:  
 if (year % 100) == 0:  
   if (year % 400) == 0:  
     print("it is a leap year")  
   else:
     print("not a leap year") 
 else:  
       print(year, " is a leap year")  
else:  
   print(year, "it is not a leap year")  
