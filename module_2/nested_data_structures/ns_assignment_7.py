students = {
   "Alice": (85, 90, 78),
   "Bob": (50, 45, 60)
}
user = input("enter a student's name:")

if user in students:
    a = students[user][0] + students[user][1] + students[user][2]
    b = a/3
    if b >= 60:
        print('Passed')
    else:
        print('Failed')
else:
    print("Student not found.")