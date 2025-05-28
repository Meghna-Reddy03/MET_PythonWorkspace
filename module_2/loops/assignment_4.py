numbers = [1,2,3,4,5,6,7,8,9,10]
sq_num = 0
for i in numbers:
    sq_num = i**2
    if i%3 != 0:
        print(sq_num)