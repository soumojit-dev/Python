n = input("Enter a number: ")
print(f"Multiplication Table of {n} is: ")

try:
    for i in range(1,11):
        print(f"{int(n)} X {i} = {int(n)*i}")
except Exception as e:
    print("An error occurred: ",e)

print("End of program!")

# TEST CASES
# Enter a number: 4
# Multiplication Table of 4 is: 
# 4 X 1 = 4
# 4 X 2 = 8
# 4 X 3 = 12
# 4 X 4 = 16
# 4 X 5 = 20
# 4 X 6 = 24
# 4 X 7 = 28
# 4 X 8 = 32
# 4 X 9 = 36
# 4 X 10 = 40

# Enter a number: S@#!
# Multiplication Table of S@#! is: 
# An error occurred:  invalid literal for int() with base 10: 'S@#!' => 'e' prints the actual Error Message that occured while program execution
# End of program!