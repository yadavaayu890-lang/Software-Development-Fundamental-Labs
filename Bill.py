name=input("Enter the item name: ")
price=int(input("Enter the price: "))
quantity=float(input("Enter the quantity: "))
subtotal=price*quantity
GST=0.15*subtotal
total=GST + subtotal
print("formatted invoice")
print(f"item name is {name}")
print(f"price is {price}")
print(f"subtotal is {subtotal}")
print(f"GST is {GST}")
print(f"total is {total}")
