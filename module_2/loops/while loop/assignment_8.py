given_list = [1,2,3,4,5]
reverse_list = []
i = -1
while i >= -len(given_list): #-1 > -5, -2 > -5
    print(i)
    reverse_list.append(given_list[i]) #given_list[-1]
    print(reverse_list)
    i -=1 #i = -3 - 1=-4
print(reverse_list)
