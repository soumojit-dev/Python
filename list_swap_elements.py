#INTERCHANGE FIRST & LAST ELEMENTS OF A LIST

def swap(lst):    #FUNCTION FOR SWAPPING ELEMENTS
    temp = lst[0]
    lst[0] = lst[-1]  #USING NEGATIVE INDEXING
    lst[-1] = temp
    return lst #RETURNS LIST AFTER SWAPPING ELEMENTS

def create_list(): #FUNCTION FOR LIST CREATION
    num = int(input("Enter number of elements in the list: "))

    new_lst = []

    for i in range(num):
        ele = int(input(f"Enter element {i+1}: "))
        new_lst.append(ele) #ADDS ELEMENTS TO THE LIST
    
    return new_lst

new_lst = create_list()
print("Original List:\n",new_lst)

swapped_lst = swap(new_lst)
print("List after swapping first & last element:\n ",swapped_lst)


# TEST CASES
# Enter number of elements in the list: 5
# Enter element 1: 23
# Enter element 2: 45
# Enter element 3: 67
# Enter element 4: 22
# Enter element 5: 90
# Original List:
#  [23, 45, 67, 22, 90]
# List after swapping first & last element:
#  [90, 45, 67, 22, 23]




