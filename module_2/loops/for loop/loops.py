person = {
    'name':'joy',
    'age': 45,
    'hobbies':['dancing','swimming','reading']
}
a = person.get('hobbies')
for item in a:
    print(item)

for key in person:
    if key == 'hobbies':
        my_hobbies = person['hobbies']
        for j in my_hobbies:
            print(j)#