year = int(input('Enter any Year: '))

if((year%4==0) and (year%100!=0) or (year%400==0)): #CONDITION FOR LEAP YEAR CHECKING
    print(year,'is a LEAP YEAR!')
else:
    print(year,'is not a LEAP YEAR!')

# TEST CASES
# Enter any Year: 2025
# 2025 is not a LEAP YEAR!

# Enter any Year: 2012
# 2012 is a LEAP YEAR!