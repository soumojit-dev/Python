def create_list():  #FUNCTION TO CREATE LIST
    num = int(input("Enter number of elements in the list: "))
    list = []

    for i in range(num):
        value = int(input(f"Enter element {i+1}: "))
        list.append(value)   #ADDS ELEMENTS
    return list

new_list = create_list()    #FUNCTION CALL
print('The LIST is: ',new_list)

rev_list = []
print('Reversed List is:')
for  item in range(len(new_list)-1,-1,-1):    #REVERSE LOGIC => range(intial,final,updation)
    rev_list.append(new_list[item])   #ADDS REVERSED ITEMS IN A NEW LIST 

print('Reversed List is:',rev_list)

# TEST CASE
# Enter number of elements in the list: 5
# Enter element 1: 32
# Enter element 2: 27
# Enter element 3: 85
# Enter element 4: 68
# Enter element 5: 92
# The LIST is:  [32, 27, 85, 68, 92]
# Reversed List is:
# Reversed List is: [92, 68, 85, 27, 32]