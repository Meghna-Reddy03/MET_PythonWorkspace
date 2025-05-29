user = input('enter 5 names: ').split()
print(user)
exist_name = input('enter:')
for i in user:
    if i == exist_name:
        print('name exists')
        break
    else:
        print("name doesn't exist")
        break
