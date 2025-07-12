#NESTED TUPLE FINDS THE HIGHEST MARKS SCORED BY A STUDENT

def create_tuple():  #FUNCTION TO CREATE NESTED TUPLE
    num = int(input("Enter number of students:"))
    temp_tup = []  #EMPTY LIST
    for i in range(num):
        name = input(f"Enter Name of Student {i+1}:")
        marks = int(input(f"Enter marks of {name}: "))
        temp_tup.append((name,marks))  #ADDS VALUE TO FORM NESTED TUPLE
    return temp_tup

std = tuple(create_tuple())
print("Student & Marks Tuple: ",std)

#key=lambda x: x[1] => tells python to compare based on 2nd item, i.e.,based on marks.
#if we write max(std) => then python will compare based on the 1st item, i.e.,based on name : alphabetical order comparison 
highest = max(std, key=lambda x: x[1])  
#             OR
# highest = student[0]
# for student in std:
#        if(student[1]>highest[1]):
#               highest = student

print(f"Topper: {highest[0]} with {highest[1]} marks.")

# TEST CASE
# Enter number of students:3
# Enter Name of Student 1:Rohan 
# Enter marks of Rohan: 37
# Enter Name of Student 2:Sam
# Enter marks of Sam: 89
# Enter Name of Student 3:John
# Enter marks of John: 83
# Student & Marks Tuple:  (('Rohan', 37), ('Sam', 89), ('John', 83))
# Topper: Sam with 89 marks.
