#Validate user login credentials.
users = {("john", "1234"): "admin", ("alice", "abcd"): "editor"}
Username = input('enter the username:')
Password = input('enter the password:')
new_tuple = (Username,Password)

if new_tuple in users:
    print("Welcome,",users[new_tuple])
else:
    print("Invalid login.")