#6Ask the user to input a word with at least 5 characters. Extract the middle 3 characters using slicing.
word = input('enter a word with 5 letters:')
middle_word = word[(len(word)//2)-1 : (len(word)//2)+2]
print(middle_word)