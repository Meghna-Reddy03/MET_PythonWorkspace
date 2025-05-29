i = 0
while i < 10:
    n = int(input('enter next number:'))
    i += 1
    if n%2 != 0:
        print('odd number')
        break    
else:
    print('all even numbers')