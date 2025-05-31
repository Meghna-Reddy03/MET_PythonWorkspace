menu = {
    'idli':10,
    'dosa':30,
    'poori':20,
    'upma':30
}
item_1 = input('Enter the item:')
item_1_count = int(input('enter the count:'))

item_1_price = menu[item_1]

bill = item_1_price*item_1_count

print(bill)
