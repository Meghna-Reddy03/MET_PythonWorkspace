temp = float(input('Enter the temperature:'))
degree = input('enter if its C or F:')
if degree.upper() == 'C':
    a = str((9/5)*temp+32)
    print(a + 'F')
elif degree.upper() == 'F':
    b = str((5/9)*temp - 32)
    print(b + 'C')
else:
    print('enter degree in celcius or fahreheit')