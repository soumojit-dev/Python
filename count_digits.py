n = int(input('Enter any number'))

#using while loop
count = 0
while(n!=0):
    n//=10
    count+=1
print("Number of digits in",n,": ",count)

#output
# Enter any number9865421
# Number of digits in 0 :  7