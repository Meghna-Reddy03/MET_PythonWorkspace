#1Ask the user to input a sentence where a word is in mixed case (e.g., “HeLLo WoRLd”). Use .swapcase() and .title() to reveal it properly.
user = input('enter a sentence:')
a = user.swapcase()
b = a.title()
print(b)