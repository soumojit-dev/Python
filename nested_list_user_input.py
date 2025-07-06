# Take marks of 3 students in 2 subjects each using NESTED LIST

stud = []   #EMPTY LIST THAT WILL STORE MARKS OF 3 STUDENTS IN 2 SUBJECTS
for i in range(3): #FOR LOOP TO ITERATE 3 TIMES FOR 3 STUDENTS
    marks  = []  #EMPTY LIST TO STORE MARKS
    print(f"Enter marks of Student {i+1}:")   
    for j in range(2):  #FOR LOOP TO ITERATE 2 TIMES FOR 2 SUBJECTS
        score = int(input(f"Subject {j+1}:")) #STORES MARKS OF 2 SUBJECTS
        marks.append(score)  #STORES 2 SUBJECT MARKS IN THE 'MARKS' 
        # marks =>[... ,...], [... ,...], [... ,...] 
    stud.append(marks)  #STORES MARKS OF 3 STUDENTS IN 2 SUBJECTS EACH
    # stud => [[... ,...], [... ,...], [... ,...]]
print("List of marks of 3 students in 2 subjects:",stud)
    
# TEST case
# Enter marks of Student 1:
# Subject 1:90
# Subject 2:97
# Enter marks of Student 2:
# Subject 1:34
# Subject 2:68
# Enter marks of Student 3:
# Subject 1:88
# Subject 2:76
# List of marks of 3 students in 2 subjects: [[90, 97], [34, 68], [88, 76]]