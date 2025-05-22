#Product Categories (Dict of Lists)
categories = {
   "clothes": ["shirt", "jeans"],
   "electronics": ["phone", "charger"]
}

user = input('enter a category name:')

if user in categories:
    print(categories[user])
else:
    print('Invalid category')