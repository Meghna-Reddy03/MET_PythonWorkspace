info = {
    'name': 'Alice', 
    'city': 'New York', 
    'hobby': 'coding'
}

for i in info.values():
    if len(i) > 5:
        print(i.upper())
    else:
        print(i.lower())