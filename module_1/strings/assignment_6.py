#4Input a sentence in all caps. Convert only the first word to title case, and the rest to lowercase. Hint: Use .capitalize() and .lower().
text = input('enter in all caps:') #THE WOODS ARE LOVELY
a = text.find(' ')
b = text[:4].capitalize()
c = text[4:].lower()
print(b+c)