n = int(input('enter a number:'))

def check_odd_even(number):
    if number%2 == 0:
        return 'even number'
    else:
        return 'odd number'

print(check_odd_even(n))