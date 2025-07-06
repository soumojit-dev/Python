rows = int(input("Enter number of rows of the matrix:"))
cols = int(input("Enter number columns of the matrix:"))

matrix = [] #EMPTY LIST
for i in range(rows): #LOOPS THROUGH EACH ROW
    row = []
    for j in range(cols): #LOOPS THROUGH EACH COLUMN
        value = int(input(f"Enter Row {i+1}, Column {j+1}:"))
        row.append(value) #ADD VALUE TO THE ROW
    matrix.append(row) #ADDS ROW TO THE MATRIX
print("----Original Matrix----")
for items in matrix:  #DISPLAYS MATRIX ROW WISE
    print(items)

transpose = []  #EMPTY LIST
for i in range(cols): #LOOPS THROUGH EACH COLUMN
    new_row = []
    for j in range(rows): #LOOPS THROUGH EACH ROW
        new_row.append(matrix[j][i]) #ROW <-> COLUMN INTERCHANGE
    transpose.append(new_row) 
print("----Transpose Matrix----")
for ele in transpose: #DISPLAYS TRANSPOSE MATRIX ROW WISE
    print(ele)

# TEST CASE
# Enter number of rows of the matrix:2
# Enter number columns of the matrix:3
# Enter Row 1, Column 1:1
# Enter Row 1, Column 2:2
# Enter Row 1, Column 3:3
# Enter Row 2, Column 1:4
# Enter Row 2, Column 2:5
# Enter Row 2, Column 3:6
# ----Original Matrix----
# [1, 2, 3]
# [4, 5, 6]
# ----Transpose Matrix----
# [1, 4]
# [2, 5]
# [3, 6]

# Enter number of rows of the matrix:2
# Enter number columns of the matrix:2
# Enter Row 1, Column 1:5
# Enter Row 1, Column 2:8
# Enter Row 2, Column 1:2
# Enter Row 2, Column 2:9
# ----Original Matrix----
# [5, 8]
# [2, 9]
# ----Transpose Matrix----
# [5, 2]
# [8, 9]