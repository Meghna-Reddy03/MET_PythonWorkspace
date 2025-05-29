number = (input('enter a number:'))
a = number.split(' ')
print(a)
search_number = (input('enter the number to search:'))
for i in a:
    if i == search_number:
        print('found')
        break
    else:
        print('not found')
        break