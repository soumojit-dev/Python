# Isogram Checker
# Problem:
# An isogram is a word with no repeating letters (case-insensitive).
# Write a function is_isogram(word) that returns True if the word or sentence of words is an isogram, otherwise False.


def is_isogram(word):  # Function to check if a word or sentence of words is an isogram
    for ch in word:
        if word.lower().count(ch) > 1:
            return False
    return True

s = input("Enter a word or a sentence: ")
sen = s.split()  # Used to split the sentence (if enetered by the user) into words

isogram = True  # Flag Variable
for word in sen: # Loop through each word's character in the sentence
    if not is_isogram(word):  
        isogram = False
        break

print(isogram)

# TEST CASES
# Enter a word or a sentence: Machine
# True

# Enter a word or a sentence: Programming
# False

# Enter a word or a sentence: The quick brown fox jumps over lazy dogs
# True