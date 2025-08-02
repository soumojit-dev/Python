# Password Strength Checker
# Problem:
# Write a function is_strong_password(pwd) that checks if a password is strong. A strong password must:
# 1. Be at least 8 characters long
# 2. Contain at least one uppercase letter
# 3. Contain at least one lowercase letter
# 4. Contain at least one digit
# 5. Contain at least one special character (like @, #, $, %, etc.)

pwd = input("Enter your password: ")
if len(pwd)<8:
    print("Minimum 8 characters needed")
else:
    upper = False
    lower = False
    digit = False
    is_special = False
    special = '@#$%&!*'

    for ch in pwd:
        if ch.isupper():
            upper = True
        elif ch.islower():
            lower = True
        elif ch.isdigit():
            digit = True
        elif ch in special:
            is_special = True
    
    if upper and lower and digit and is_special:
        print("Strong Password")
    else:
        print("Weak Password")
        if not upper:
            print("At least one uppercase letter")
        if not lower:
            print("At least one lowercase letter")
        if not digit:
            print("At least one digit")
        if not is_special:
            print("At least one special character")

# TEST CASES
# Enter your password: MyPass123!
# Strong Password

# Enter your password: mypassword
# Weak Password
# At least one uppercase letter
# At least one digit
# At least one special character