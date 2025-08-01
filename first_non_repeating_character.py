s = input("Enter a sentence: ").lower()
for char in s:
    if s.count(char) == 1:
        print(f"'{char}' is the first non repeating character")
    
# TEST CASES
# Enter a sentence: Sosimimuu
# 'o' is the first non repeating character

# Enter a sentence: MaNA
# 'm' is the first non repeating character
# 'n' is the first non repeating character
