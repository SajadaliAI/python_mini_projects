foods  =[]
prices =[]
total  =0
while True:
    food = input("Enter the food buy to(q to quit): ")
    if food =="q":
        break
    else:
        price=float(input(f"enter the price of {food}$ "))
        foods.append(food)
        prices.append(price)
print("____YOUR CART____")
for food in foods:
    print(food,end=" ")
for price in prices:
    total +=price 
print()
print(f"your total amount is: ${total} ")