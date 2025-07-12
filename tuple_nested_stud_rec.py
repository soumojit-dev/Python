# store each student's data in this format:
# (name, roll, marks1, marks2, marks3)
# Perform the following:
# 1. sorting by roll numbers
# 2. sorting by total marks (highest -> lowest)

def create_tuple():
    num = int(input("Enter number of students:"))
    temp_tup = []
    for i in range(num):
        print(F"Enter Details of Student {i+1}:")
        name = input("Name:")
        roll = int(input(f"Roll No. of {name}:"))
        marks_1 = int(input("Marks of Sub 1: "))
        marks_2 = int(input("Marks of Sub 2: ")) 
        marks_3 = int(input("Marks of Sub 3: "))
        temp_tup.append((name,roll,marks_1,marks_2,marks_3))
    return temp_tup

records = tuple(create_tuple())
print(f"Student Records : {records}")

#sort by roll numbers
sort_roll = tuple(sorted(records, key=lambda x: x[1]))
print("Sorted by Roll Numbers: ",sort_roll)

#sort by total marks(highest -> lowest)
sort_total_marks = tuple(sorted(records, key=lambda x: x[2]+x[3]+x[4], reverse=True))

for s in sort_total_marks:
    total = s[2]+s[3]+s[4]
    print(f"{s[0]} (Roll:{s[1]} -> Total: {total})")

# TEST CASE
# Enter number of students:3
# Enter Details of Student 1:
# Name:Pedro
# Roll No. of Pedro:24
# Marks of Sub 1: 76  
# Marks of Sub 2: 89
# Marks of Sub 3: 66
# Enter Details of Student 2:
# Name:Kendrick
# Roll No. of Kendrick:11
# Marks of Sub 1: 88
# Marks of Sub 2: 73
# Marks of Sub 3: 90
# Enter Details of Student 3:
# Name:Tyla
# Roll No. of Tyla:41
# Marks of Sub 1: 75
# Marks of Sub 2: 49
# Marks of Sub 3: 72
# Student Records : (('Pedro', 24, 76, 89, 66), ('Kendrick', 11, 88, 73, 90), ('Tyla', 41, 75, 49, 72))
# Sorted by Roll Numbers:  (('Kendrick', 11, 88, 73, 90), ('Pedro', 24, 76, 89, 66), ('Tyla', 41, 75, 49, 72))    
# Kendrick (Roll:11 -> Total: 251)
# Pedro (Roll:24 -> Total: 231)
# Tyla (Roll:41 -> Total: 196)





                      
        