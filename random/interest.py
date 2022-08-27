principal = int(input("Enter principal: "))
rate = int(input("Enter interest rate: ")) / 100
simple = principal * rate * 3
compound = (principal*(1+rate)**3) - principal
print("Simple:", simple, "Compound:", compound, "Difference:", compound-simple)
