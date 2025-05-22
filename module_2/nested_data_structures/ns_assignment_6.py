order = {
   "item1": {"name": "Laptop", "price": 700},
   "item2": {"name": "Mouse", "price": 20}
}
user = input('enter an item key:')
if user == "item1":
    print(order["item1"])
elif user == "item2":
    print(order["item2"])
else:
    print("Item not found.")