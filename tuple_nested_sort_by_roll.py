def create_tuple(): #FUNCTION TO CREATE NESTED LIST
    num = int(input("Enter number of students:"))
    temp_tup = []
    for items in range(num):
        name = input(f"Enter Name of Student {items + 1}:")
        roll = int(input(f"Enter Roll No. of {name}:"))
        temp_tup.append((name,roll)) #FORMS NESTED LIST
    return temp_tup

std = tuple(create_tuple())
print("Student Name & Roll Numbers: ",(std))

#Ascending order sorting
asc = sorted(std, key= lambda x: x[1])  #Key= lambda x: x[1] => sorting based on Roll Numbers

#Descending order sorting
desc = sorted(std, key=lambda x: x[1], reverse=True) #Key= lambda x: x[1] => sorting based on Roll Numbers
print(f"{asc} is the Ascending order sorting")
print(f"{desc} is the Descending order sorting")

#TEST CASE
# Enter number of students:4
# Enter Name of Student 1:Sam
# Enter Roll No. of Sam:78
# Enter Name of Student 2:John
# Enter Roll No. of John:91
# Enter Name of Student 3:Rohan
# Enter Roll No. of Rohan:85
# Enter Name of Student 4:Lewis
# Enter Roll No. of Lewis:65
# Student Name & Roll Numbers:  (('Sam', 78), ('John', 91), ('Rohan', 85), ('Lewis', 65))
# (('Lewis', 65), ('Sam', 78), ('Rohan', 85), ('John', 91)) is the Ascending order sorting
# (('John', 91), ('Rohan', 85), ('Sam', 78), ('Lewis', 65)) is the Descending order sorting