total_amount = int(input('Enter the total amount:'))

if total_amount > 100:
    a = (10/total_amount)*100
    final_amt = str(total_amount - a)
    print('your final amount is ' + '$' + final_amt)

elif (total_amount > 50) and (total_amount < 100):
    b = (5/total_amount)*100
    final_amt2 = str(total_amount - b)
    print('your final amount is ' + '$' + final_amt2)
else:
    print('no discount')
