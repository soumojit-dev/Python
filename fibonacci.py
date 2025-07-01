n = int(input('Enter how many terms you want: '))
a = 0
b = 1

print('Fibonacci Series:')
print(a)
print(b)

for i in range(2, n):  
    c = a + b
    print(c)
    a = b
    b = c


# TEST CASES
# Enter how many terms you want: 10
# Fibonacci Series:
# 0
# 1
# 1
# 2
# 3
# 5
# 8
# 13
# 21
# 34