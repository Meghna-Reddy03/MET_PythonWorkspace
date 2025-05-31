list = ['python', 'code', 'loop', 'if', 'python', 'else', 'if']#
stop_words={'if','else'}
a=set()
for i in list:
    if i not in stop_words:
        a.add(i)
print(a)
        

