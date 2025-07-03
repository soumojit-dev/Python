def create_list(): #FUNCTION FOR LIST CREATION
    num = int(input("Enter number elements in the list: "))
    list = []

    for i in range(num):
        ele = int(input(f"Enter the elements {i+1}: "))
        list.append(ele)
    return list

new_list = create_list()   #FUNCTION CALLING
print('The List is:\n',new_list)

count = 0
value = int(input("Enter the SEARCH VALUE to count it's occurence in the list: "))
for i in range(len(new_list)):
    if(value == new_list[i]):   #CONDITION TO CHECK WHETHER THE ENETERED VALUE MATCHES ELEMENTS IN THE LIST OR NOT
        count+=1  #COUNTS THE OCCURENCE

if(count>0):
    print("Occurence of the SEARCH VALUE: ",count)
else:
    print(value,'NOT FOUND!')   #INVALID USER INPUT

# TEST CASES
# Enter number elements in the list: 5
# Enter the elements 1: 23
# Enter the elements 2: 45
# Enter the elements 3: 65
# Enter the elements 4: 23
# Enter the elements 5: 23
# The List is:
#  [23, 45, 65, 23, 23]
# Enter the SEARCH VALUE to count it's occurence in the list: 23
# Occurence of the SEARCH VALUE:  3

# Enter number elements in the list: 3
# Enter the elements 1: 23
# Enter the elements 2: 12
# Enter the elements 3: 23
# The List is:
#  [23, 12, 23]
# Enter the SEARCH VALUE to count it's occurence in the list: 9
# 9 NOT FOUND!
