from datetime import datetime  #module

year = int(input("Enter the Year:"))
month = int(input("Enter the Month:"))
date = int(input("Enter the Date:"))

my_date = datetime(year,month,date) #datetime()` function creates the date object with the numbers enetred

day_name = my_date.strftime("%A")  #"%A" => format specifier

print("Day Name:",day_name)

# TEST CASES
# Enter the Year:2025
# Enter the Month:7
# Enter the Date:13
# Day Name: Sunday

# Enter the Year:2005
# Enter the Month:08
# Enter the Date:19
# Day Name: Friday

# Enter the Year:2028
# Enter the Month:8 
# Enter the Date:19
# Day Name: Saturday

# Enter the Year:2024
# Enter the Month:7
# Enter the Date:15
# Day Name: Monday