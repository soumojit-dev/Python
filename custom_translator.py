def translate(phrase):
    translation = " "
    for ch in phrase:
        if ch in "AEIOUaeiou":
            translation += 's'
        else:
            translation += ch
    return translation

print("----Welcome to Custom Translator----")
print(translate(input("Enter word/sentence: ")))

# TEST CASES
# ----Welcome to Custom Translator----
# Enter word/sentence: Banking
#  Bsnksng

# ----Welcome to Custom Translator----
# Enter word/sentence: I love Python and its Libraries
#  s lsvs Pythsn snd sts Lsbrsrsss