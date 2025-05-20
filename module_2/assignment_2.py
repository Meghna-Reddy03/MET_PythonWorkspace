details = {
    "username" : "Meghna24",
    "password" : "1a34"
}
user = input('enter your username:')
password = input('enter your password:')

correct_username = details.get('username')
correct_password = details.get('password')

if user == correct_username:
    if password == correct_password:
        print('succesful login')
else:
    print('invalid credentials')