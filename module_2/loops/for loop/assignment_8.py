num =  [10, 25, 36, 40]
for i in num:
    for a in [1,2,3,4,5,6,7,8]:
        if a*a == i:
            print(i,' is a perfect square')
            break
    else:
        continue
    break
        