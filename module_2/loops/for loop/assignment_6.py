data={'apple': 2,'banana':3,'apricot':4,'berry':5}#
prod=1
for key,value in data.items():
    if key[0]=='a':
        prod*=value
print(prod)