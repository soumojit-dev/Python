def create_list():  #FUNCTION TO CREATE LIST
    num = int(input("Enter number of elements in the list: "))
    list = []

    for i in range(num):
        value = input(f"Enter element {i+1}: ")
        list.append(value)   #ADDS ELEMENTS
    return list

new_list = create_list()    #FUNCTION CALL
print('The LIST is: ',new_list)

str =""  #EMPTY STRING
for i in new_list:
    str+=i + " "   #ADDS LIST ITEMS WITH SPACES(" ") IN BETWEEN IN STR VARIABLE AS A STRING
print("String version of the List:",str)


# TEST CASE
# Enter number of elements in the list: 7
# Enter element 1: Python
# Enter element 2: is
# Enter element 3: the
# Enter element 4: language
# Enter element 5: of
# Enter element 6: the
# Enter element 7: future
# The LIST is:  ['Python', 'is', 'the', 'language', 'of', 'the', 'future']
# String version of the List:       Python is the language of the future 