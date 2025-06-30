num = int(input('Enter any number: '))

rev = 0
#using while loop
while(num!=0):
    rem = num%10
    rev = rev*10+rem
    num//=10
print('Reversed Number:',rev)

#OUTPUT
# Enter any number: 19452
# Reversed Number: 25491