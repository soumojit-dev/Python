str = input("Enter a string: ").lower()
v = 0 #vowels 
c = 0 #consonants
for ch in str:
    if(ch in 'aeiou'):
        v+=1
    else:
        c+=1
print("Vowels: ",v)
print("Consonants: ",c)

# TEST CASES
# Enter a string: Python Dev Community
# Vowels:  5
# Consonants:  15

