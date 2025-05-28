students_db = {
    'grading_scales': {
        'percentage': {
            'Math': {'min': 97, 'max': 100, 'grade': 'A'},
            'Science': {'min': 93, 'max': 96, 'grade': 'A+'},
            'English': {'min': 90, 'max': 92, 'grade': 'A++'},
            'History': {'min': 87, 'max': 89, 'grade': 'B'},
            'Physics': {'min': 83, 'max': 86, 'grade': 'B+'},
        }
    }
}
subject  = input('enter the subject:')
marks = int(input('enter your marks:'))
data = students_db['grading_scales']['percentage']

if subject in data:
    marks_obtained = data[subject]
    if marks >= marks_obtained['min'] and marks <= marks_obtained['max']:
        print(f"Your grade is {marks_obtained['grade']}")
        print(f"You have passed the {subject}")
    else:
        print(f'You have not passed the {subject}')
