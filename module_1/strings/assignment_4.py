#2Input a sentence. Convert all characters to uppercase and then reverse the string.

text = input('enter a sentence:')
a = text.upper()
b = a[::-1]
print(b)