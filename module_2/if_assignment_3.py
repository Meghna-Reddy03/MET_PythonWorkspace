num = int(input('enter the number:'))
secret_number = 55
if num == secret_number:
    print('You have guessed it correctly!')
elif num > secret_number:
    print('the number is too high')
elif num < secret_number:
    print('the number is too low')