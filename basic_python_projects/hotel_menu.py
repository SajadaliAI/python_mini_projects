
menu={
    "piza"  :40,
    "pasta" :50,
    "burger":60,
    "saland":70,
    "coffe" :80
}
print("Wellcome to Python restaurant")
print("piza : Rs 40\npasta: Rs 50\nburger:Rs 60\nsaland:Rs 70\ncoffe: Rs 80")
order_total=0
item_1= input("Enter name of item you want to order= ")
if item_1 in menu:
    order_total+= menu[item_1]
    print(f"your item {item_1} has been added to your order")
else:
    print(f"order item {item_1} is not available yet!")
another_order=input("Do you want to add another item?(yes/no)") 
if another_order=="yes":
    item_2=input("Enter the name of second item= ")
    if item_2 in menu:
        order_total+=menu[item_2]
        print(f"item {item_2}has been added to your  order")
    else:
        print(f"ordered item {item_2} is not availabbe yet!")
print(f"total amount of items to pay is {order_total}")

