data =[{
    'name':"Meghna",
    'age':21
},
{
    'name':"anita",
    'age':24
}]

def extracted_names(details):
    name_1 = details[0]['name']
    name_2 = details[1]['name']
    return [name_1,name_2]

def extracted_age(info):
    age_1=info[0]['age']
    age_2=info[1]['age']
    return [age_1,age_2]

names = extracted_names(data)
ages = extracted_age(data)

print(names)
print(ages)