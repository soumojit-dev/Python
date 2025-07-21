sent = input("Enter a sentence: ")
words = sent.split()

word_count = {}

for word in words:  # <- this was the mistake (you had: for word in word_count)
    word = word.lower()
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print("Word Frequencies:")
for word, count in word_count.items():
    print(f"{word} : {count}")

# TEST CASE
# Enter a sentence: Python is fun and python is easy
# Word Frequencies:
# python : 2
# is : 2
# fun : 1
# and : 1
# easy : 1

