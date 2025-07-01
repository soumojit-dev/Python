num1 = int(input('Enter the first number (A): '))
num2 = int(input('Enter the second number (B): '))

#logic
num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2

print("After swapping, A =",num1,'and B =',num2)

# TEST CASES
# Enter the first number (A): 24
# Enter the second number (B): 56
# After swapping, A = 56 and B = 24

# Algorithm
# A = 24, B = 56
# STEP 1: A = A + B => A = 24 = 56 => A = 80
# STEP 2: B = A - B => B = 80 - 56 => B = 24 (SWAPPED)
# STEP 3: A = A - B => A = 80 - 24 => A = 56 (SWAPPED)
# Now,
#    A = 56, B = 24
