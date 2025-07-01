num = int(input("Enter any number: "))
print("You entered:", num)

orgnum = num
sum = 0

while orgnum != 0:
    sum += orgnum % 10
    orgnum //= 10

if sum % 3 == 0 and sum % 5 == 0:
    print(num, "is a MAGIC NUMBER")
else:
    print(num, "is not a MAGIC NUMBER")


# TEST CASES
# Enter any number: 555
# You entered: 555
# 555 is a MAGIC NUMBER

# Enter any number: 1234
# You entered: 1234
# 1234 is not a MAGIC NUMBER