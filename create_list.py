lst = []
num = int(input("Enter number of elements: "))

for i in range(num):
    ele = int(input(f"Enter element {i+1}: ")) #f (f-string) in Python — it's just a convenient and modern way to insert variables into strings.
    lst.append(ele) #adds elements

print("The List: ",lst) #prints the list



# OUTPUT
# Enter number of elements: 5
# Enter element 1: 24
# Enter element 2: 45
# Enter element 3: 62
# Enter element 4: 71
# Enter element 5: 62
# The List:  [24, 45, 62, 71, 62]