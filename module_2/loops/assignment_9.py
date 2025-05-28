names = ('sam', 'john', 'alex', 'bob')
for i in names:
    if len(i) <= 3:
        print(i.upper())
    else:
        print(i.capitalize())