num = int(input("Enter any number: "))

original_num = num 

#count no. of digits
count = 0
while(original_num!=0):
    original_num//=10
    count+=1

original_num = num #reset
sum = 0

while(original_num!=0):
    rem = original_num%10  #remainder
    sum+=pow(rem,count)
    original_num//=10

if(sum == num):
    print(num,"is an Armstrong number")
else:
    print(num,"is not an Armstrong number")


# TEST CASES
# Enter any number: 153
# 153 is an Armstrong number

# Enter any number: 555
# 555 is not an Armstrong number