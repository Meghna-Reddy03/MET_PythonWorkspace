#5Ask the user to input a password. Replace all vowels with * and print it.
password = input('enter your password:')
a = password.replace('a','*')
b = a.replace('e','*')
c = b.replace('i','*')
d = c.replace('o','*')
e = d.replace('u','*')
print(e)