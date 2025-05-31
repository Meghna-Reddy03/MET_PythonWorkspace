num1 = int(input('enter 1st number:'))
num2 = int(input('enter 2nd number:'))
operation = input('enter the operation:')
#
def add(a,b):
    print(a+b)
def sub(a,b):
    print(a-b)
def multiply(a,b):
    print(a*b)
def divide(a,b):
    print(a/b)

if operation == '+':
    add(num1,num2)
elif operation == '-':
    sub(num1,num2)
elif operation == '*':
    multiply(num1,num2)
elif operation == '/':
    divide(num1,num2)
else:
    print("invalid operation")    