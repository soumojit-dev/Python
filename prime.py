n = int(input('Enter a number: '))
isPrime = True
for i in range(2,n):
    if(n%i==0):
        isPrime = False
        break

if(not isPrime):
    print(n,'is a not PRIME NUMBER')
else:
    print(n,'is a PRIME NUMBER')


# TEST CASES
# Enter a number: 11
# 11 is a PRIME NUMBER

# Enter a number: 4
# 4 is a not PRIME NUMBER