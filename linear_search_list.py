num = int(input("Enter the number of elements in the list: "))
lst = []

for i in range(num):
    ele = int(input(f"Enter element {i+1}: "))
    lst.append(ele) #ADDS ELEMENTS

print("The List is:\n",lst)

val = int(input("Enter the SEARCH VALUE: "))  #ASKS USER FOR THE ELEMENT TO SEARCH

#lINEAR SEARCH
found = False #FLAG VARIABLE
for i in range(len(lst)):
    if(val == lst[i]):
        print(val,'is located at index',i)
        found = True
        break #EXITS LOOP AFTER GETTING THE FIRST MATCH

if not found:
    print(val,'NOT FOUND!') #ELSE PART


# TEST CASES
# Enter the number of elements in the list: 5
# Enter element 1: 12
# Enter element 2: 34
# Enter element 3: 56
# Enter element 4: 78
# Enter element 5: 92
# The List is:
#  [12, 34, 56, 78, 92]
# Enter the SEARCH VALUE: 56
# 56 is located at index 2

# Enter the number of elements in the list: 4
# Enter element 1: 23
# Enter element 2: 45
# Enter element 3: 21
# Enter element 4: 67
# The List is:
#  [23, 45, 21, 67]
# Enter the SEARCH VALUE: 10
# 10 NOT FOUND!


