cp=float(input("Enter cost price:"))
sp=float(input("Enter selling price:"))

if sp>cp:
    profitper=((sp-cp)/cp)*100
    print("Profit incurred is",profitper,"%")
elif cp>sp:
    lossper=((cp-sp)/cp)*100
    print("Loss incurred is",lossper,"%")


    
