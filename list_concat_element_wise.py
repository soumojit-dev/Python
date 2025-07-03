def create_list(list_name): #FUNCTION TO CREATE NEW LIST
    num = int(input(f"Enter number of elements in {list_name}: "))  
    lst = []
    print(f"Enter elements for {list_name}")
    for i in range(num):
        ele = input(f"Enter element {i+1}: ")
        lst.append(ele)
    return lst

def merge_list(lst_1,lst_2):  #FUNCTION TO MERGE THE LISTS
     result = []  #STORES THE MERGED LIST
     if len(lst_1)!=len(lst_2):   #CHECKS BOTH LIST LENGTH IS EQUAL OR NOT
         print("List of Unequal Lengths. INVALID!")   
         return None
     else:
         for i in range(len(lst_1)):
          result.append(lst_1[i] + lst_2[i])   #MERGES THE LIST ELEMENT WISE
     return result



lst_1 = create_list("List 1")   #FUNCTION CALLING
lst_2 = create_list("List 2")   #FUNCTION CALLING

merged = merge_list(lst_1,lst_2)    #FUNCTION CALLING

print("List after merging element wise: ", merged)


# TEST CASES
# Enter number of elements in List 1: 2                
# Enter elements for List 1
# Enter element 1: 8       
# Enter element 2: 5
# Enter number of elements in List 2: 4
# Enter elements for List 2
# Enter element 1: S
# Enter element 2: T
# Enter element 3: R
# Enter element 4: W
# List of Unequal Lengths. INVALID!
# List after merging element wise:  None

# Enter number of elements in List 1: 4
# Enter elements for List 1
# Enter element 1: 6       
# Enter element 2: 9
# Enter element 3: 8
# Enter element 4: 7
# Enter number of elements in List 2: 4
# Enter elements for List 2
# Enter element 1: P
# Enter element 2: Q
# Enter element 3: R
# Enter element 4: S
# List after merging element wise:  ['6P', '9Q', '8R', '7S']