def create_dic():
    n = int(input("Enter number of students: "))
    dic = {}
    for i in range(n):
        name = input(f"Enter name of Student {i+1}: ")
        marks = input(f"Enter Marks of {name}: ")
        dic[name] = marks
    return dic

std_dic = create_dic()
print(f" Student's Marks Dictionary : {std_dic}")

#KEY SEARCH
value = input("Enter Name of the Student: ")

if value in std_dic:
    print(f"{value}'s marks = {std_dic[value]}")
else:
    print(f"{value} not found.")


# TEST CASE
# Enter number of students: 3
# Enter name of Student 1: Bob
# Enter Marks of Bob: 86
# Enter name of Student 2: Charlie
# Enter Marks of Charlie: 73
# Enter name of Student 3: John
# Enter Marks of John: 94
#  Student's Marks Dictionary : {'Bob': '86', 'Charlie': '73', 'John': '94'}
# Enter Name of the Student: John
# John's marks = 94

# Enter number of students: 2
# Enter name of Student 1: Lewis
# Enter Marks of Lewis: 66
# Enter name of Student 2: Puta
# Enter Marks of Puta: 89
#  Student's Marks Dictionary : {'Lewis': '66', 'Puta': '89'}
# Enter Name of the Student: John
# John not found.