cart = [{"id": 1, "name": "Shirt", "qty": 1}]

product_id = int(input('enter the id:'))
product_name = input('enter the name of the product:')

product = {
    'id': product_id,
    'name': product_name,
}

if product['id'] == cart[0]['id']:
        print('Item already in cart')
else:
        cart.append(product)
        print(cart)