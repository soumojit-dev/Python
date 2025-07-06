#3x3 matrix creation using nested list
matrix = []
for i in range(3): # Loop through 3 rows
    row = []   # Empty list to store elements of this row
    print(f"Enter 3 elements in Row {i+1}:")
    for j in range(3): # Loop through 3 columns
        col = int(input(f"Value of Column {j+1}:"))
        row.append(col)
    matrix.append(row)
    
print("3x3 Matrix using Nested List:") #CAN ALSO PRINT THE NESTED LIST HERE DIRECTLY
for row in matrix: #OPTIONAL PART. USE ONLY IF YOU WANT TO DISPLAY IT ROW WISE
    print(row)  #prints the matrix row wise

# TEST CASE
# Enter 3 elements in Row 1:
# Value of Column 1:1
# Value of Column 2:2
# Value of Column 3:3
# Enter 3 elements in Row 2:
# Value of Column 1:4
# Value of Column 2:5
# Value of Column 3:6
# Enter 3 elements in Row 3:
# Value of Column 1:7
# Value of Column 2:8
# Value of Column 3:9
# 3x3 Matrix using Nested List:
# [1, 2, 3]
# [4, 5, 6]
# [7, 8, 9]