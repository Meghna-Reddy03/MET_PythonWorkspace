user_keys1 = input('enter students name:')
user_keys2 = input('enter students name:')
user_keys3 = input('enter students name:')
user_values1 = input('enter students marks:')
user_values2 = input('enter students marks:')
user_values3 = input('enter students marks:')

report = {
    user_keys1 : user_values1,
    user_keys2 : user_values2,
    user_keys3 : user_values3
}

maximum_marks = max(report.values())

print("the max marks is ",maximum_marks)

for student,marks in report.items():
    if marks == maximum_marks:
        print("The student with the highest marks is:", student)
        break