#element substitution/replacing/insertion using slicing

def create_list():    #Function for list creation
    num = int(input("Enter number of elements: "))
    list = []
    for i in range(num):
        value = input(f"Enter element {i+1}: ")
        list.append(value)   #ADDS ELEMENTS TO THE LIST
    return list

new_list = create_list()
print('Original List: ',new_list)

#element substitution using slicing
index = int(input('Enter the index for substitution: '))    
element = input(f"Enter the element for substitution: ")
new_list = new_list[:index] + [element] + new_list[index + 1:]   #SUBSTITUTION LOGIC USING SLICING
print('List after substitution:',new_list)

# ALGORITHM
# new_list = ['Rohan', 'Mango', 'Kiwi', 'Grapes']
# index = 1
# new_list[:1] => ['Rohan']
# [element] => ['Apple']
# new_list[2:] => ['Kiwi', 'Grapes']
# new_list = new_list[:index] + [element] + new_list[index + 1:]
# So after operation, new_list = ['Rohan', 'Apple', 'Kiwi', 'Grapes']

# TEST CASES
# Enter number of elements: 2
# Enter element 1: Ashay
# Enter element 2: OMG
# Original List:  ['Ashay', 'OMG']
# Enter the index for substitution: 1
# Enter the element for substitution: 2005
# List after substitution: ['Ashay', '2005'] => replaced 'OMG' with '2005'

# Enter number of elements: 2
# Enter element 1: USA
# Enter element 2: INDIA
# Original List:  ['USA', 'INDIA']
# Enter the index for substitution: 0
# Enter the element for substitution: CHINA
# List after substitution: ['CHINA', 'INDIA'] replaced 'USA' with 'CHINA'

# Enter number of elements: 3
# Enter element 1: Django
# Enter element 2: Flask
# Enter element 3: Docker
# Original List:  ['Django', 'Flask', 'Docker']
# Enter the index for substitution: 3
# Enter the element for substitution: Kubernetes
# List after substitution: ['Django', 'Flask', 'Docker', 'Kubernetes']  inserted at the end of the list

