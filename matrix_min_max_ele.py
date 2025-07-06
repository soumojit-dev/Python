rows = int(input("Enter number of rows in the matrix:"))
cols = int(input("Enter number of columns in the matrix:"))

matrix = [] #EMPTY LIST
for i in range(rows): #LOOPS THROUGH EACH ROW
    row = []
    for j in range(cols):  #LOOPS THROUGH EACH COLUMN
        value = int(input(f"Enter Row {i+1},Column {j+1}:"))
        row.append(value)  #ADD VALUE TO THE ROW
    matrix.append(row)  #ADDS ROW TO THE MATRIX
print("Original Matrix")
for k in matrix:  #DISPLAYS MATRIX ROW WISE
    print(k)

#flattening the matrix =>multi-dimensional to a single list
flat = []
for row in matrix: #GOES THROUGH EACH ROW IN THE MATRIX
    for item in row:  #GOES THROUGH EACH ELEMENT IN THE ROW
        flat.append(item)
print("Flattend List:",flat)

#assumption for maximum element
max = flat[0]
min = flat[0]
for val in flat: #LOOPS THROUGH EACH ELEMENT
    if val > max:
        max = val  #UPDATE IF VALUE IS GREATER THAN THE ASSUMPTION
for val in flat: #LOOPS THROUGH EACH ELEMENT
    if val < min:
        min = val  #UPDATE IF VALUE IS SMALLER THAN THE ASSUMPTION

print("Maximum Element:",max)
print("Minimum Element:",min)

# TEST CASE
# Enter number of rows in the matrix:2
# Enter number of columns in the matrix:3
# Enter Row 1,Column 1:5
# Enter Row 1,Column 2:4
# Enter Row 1,Column 3:7
# Enter Row 2,Column 1:9
# Enter Row 2,Column 2:2
# Enter Row 2,Column 3:1
# Original Matrix
# [5, 4, 7]
# [9, 2, 1]
# Flattend List: [5, 4, 7, 9, 2, 1]
# Maximum Element: 9
# Minimum Element: 1