s = input("Enter a sentence: ")
freq = {}

for char in s:
    if char in freq and char!=" ": # => 'char' ignores spaces in the sentence
        freq[char]+= 1
    else:
        freq[char] = 1

print(f"Character Frequencies: {freq}") #=>DISPLAYS IN DICTIONARY FORM
            #OR
# print("Character Frequencies: ")
# for char, count in freq.items():
#     if char!=" ": => IGNORES SPACES IN THE SENTENCE
#        print(f"{char}: {count}")

# TEST CASES
# Enter a sentence: This is my pen
# Character Frequencies: {'T': 1, 'h': 1, 'i': 2, 's': 2, ' ': 1, 'm': 1, 'y': 1, 'p': 1, 'e': 1, 'n': 1}
       #OR
# Enter a sentence: This is my pen
# Character Frequencies: 
# T: 1
# h: 1
# i: 2
# s: 2
# m: 1
# y: 1
# p: 1
# e: 1
# n: 1
