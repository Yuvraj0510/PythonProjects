unit=int(input("Number of units used: "))
if(unit<=100):
    print("No Bill")
elif(100<unit<=200):
    print("Your bill is : ₹", (unit-100)*5)
else:
    print("Your bill is : ₹", 500+(unit-200)*10)
