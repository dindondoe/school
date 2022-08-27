month = { "january" : 31 , "february" : 28 , "march" : 31 , "april" : 30 , "may" : 31 , "june" : 30 , "july" : 31 , "august" : 31 , "september" : 30 , "october" : 31 , "november" : 30 , "december" : 31}

mon = input("Enter the month name: ")

print("Number of days in ",mon,"=",month [ mon ])

lst = list ( month . keys() )

lst.sort()

print( "The months which have the same number of days: ")

for i in month :

    if month [ i ] == month[mon] :

        print( i )


