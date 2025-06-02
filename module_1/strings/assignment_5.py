#3Ask the user to enter a sentence. Count how many times “a”, “e”, and “i” appear using .count() and sum them using str() + int().
user = input('enter a sentence:')
a = int(user.count('a'))
b = int(user.count('e'))
c = int(user.count('i'))
print(a+b+c)
