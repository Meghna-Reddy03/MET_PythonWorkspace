tags = {"python", "fastapi", "backend"}
a = input('enter a new tag:')
if a in tags:
    print('it already exists')
else:
    tags.add(a)
    print(tags)