# Find the Longest Palindromic Word
# Problem: Given a sentence, find and return the longest palindromic word.

def is_palin(word):
    return word == word[::-1]  # Check if word is same as its reverse

s = input("Enter a sentence: ")
words = s.split()  # Split sentence into words

longest_palin = ""

for word in words:
    if is_palin(word) and len(word) > len(longest_palin):
        longest_palin = word

if longest_palin:
    print("Longest palindromic word:", longest_palin)
else:
    print("No palindromic word found.")

# TEST CASES
# Enter a sentence: madam racecar apple kayak noon
# Longest palindromic word: racecar

# Enter a sentence: Was it a car or a cat I saw
# Longest palindromic word: a

# Enter a sentence: hello python science apple banana
# No palindromic word found.