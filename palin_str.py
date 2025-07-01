str = input("Enter a string: ")

length = len(str)

isPalin = True #FLAG VARIABLE
i = 0
while(i<length//2): #CHECKS ONLY TILL THE HALFWAY
    if(str[i]!=str[length-i-1]):
        isPalin = False
        break
    i+=1

if(isPalin):
    print("PALINDROME WORD")
else:
    print("Not a PALINDROME WORD")

# OUTPUT
# Enter a string: radar
# PALINDROME WORD

# Enter a string: apple
# Not a PALINDROME WORD