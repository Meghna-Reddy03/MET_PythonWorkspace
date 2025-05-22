#Store unique GPS coordinates.
locations = [(12.9716, 77.5946)]
Latitude =  float(input('enter the latitude value:'))
Longitude = float(input('enter the longitude value:'))

user_locations = (Latitude,Longitude)

if user_locations in locations:
    print("Location already exists.")
else:
    locations.append(user_locations)
    print(locations)