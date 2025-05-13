
unit=input("Is this tempreture celcius or fahrenheight (C/F): ")
temp=float(input("Enter the temprature: "))
if temp =="C":
    temp=round(( temp * 9) / 5 + 32,1)
    print(f"the temprature in fahreinheit is: {temp} °f")
elif unit=="F":
    temp=round((temp - 32) * 5 / 9,1)
    print(f"the temprature in celcius is :{temp} °c ")
else:
    print(f"{unit} is an invalid unit of meaurement")











