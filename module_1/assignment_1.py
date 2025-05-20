'''Ask user to enter 16 digit credit card number
Print out in following format - XXXX XXXX XXXX 2345
Basically, mask all the digits except last 4 digits
 '''
user = input('enter the digits:')
last_digits = user[16:]
