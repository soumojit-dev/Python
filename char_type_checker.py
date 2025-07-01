ch = input('Enter a character: ')
print(ch)

print('-----CHARACTER TYPE CHECKER-----\n')
if(ch.isupper()):
    print('UPPERCASE CHARACTER IDENTIFIED!')
elif(ch.islower()):
    print('LOWERCASE CHARACTER IDENTIFIED!')
elif(ch.isdigit()):
    print('DIGIT CHARACTER IDENTIFIED!')
elif(ch in '$!@#&'):
    print('SPECIAL CHARACTER IDENTIFIED!')
else:
    print("UNIDENTIED CHARACTER!")

#TEST CASES
# Enter a character: HELLO
# HELLO
# -----CHARACTER TYPE CHECKER-----

# UPPERCASE CHARACTER IDENTIFIED!

# Enter a character: @
# @
# -----CHARACTER TYPE CHECKER-----

# SPECIAL CHARACTER IDENTIFIED!