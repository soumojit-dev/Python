def create_tuple(): #FUNCTION FOR CREATING A TUPLE
    num = int(input("Enter number of elements:"))
    temp_tup =[]   #EMPTY LIST
    for i in range(num):
        value = input(f"Enter Element {i+1}:")
        temp_tup.append(value)   #ADDS VALUE TO THE LIST
    new_tup = tuple(temp_tup)    #LIST -> TUPLE CONVERSION
    return new_tup
tup1 = create_tuple()
print("Tuple: ",tup1)

search = input("Enter the elements to copy: ")
list_t = []
for items in tup1:
    if items in search:
        list_t.append(items)

tup2 = tuple(list_t)
print(f"Tuple of the specific element is {tup2}")

# TEST CASE
# Enter number of elements:5
# Enter Element 1:23
# Enter Element 2:42
# Enter Element 3:36
# Enter Element 4:78
# Enter Element 5:91
# Tuple:  ('23', '42', '36', '78', '91')
# Enter the elements to copy: 23 36 78
# Tuple of the specific element is ('23', '36', '78')

