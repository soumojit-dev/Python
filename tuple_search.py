# Tuples are immutable, so once created, you cannot change individual elements directly.
# We use a list first because we can't add elements directly to a tuple while taking inputs.

def create_tuple(): #FUNCTION TO CREATE A TUPLE FROM A LIST
    num = int(input("Enter number of elements in the tuple:"))
    temp_tup = []  #EMPTY LIST 
    for i in range(num):
        value = input(f"Enter Element {i+1}:")
        temp_tup.append(value)   #VALUE ADDED TO THE LIST
    new_tup = tuple(temp_tup)   #LIST -> TUPLE CONVERSION
    return new_tup

tup = create_tuple()
print("Tuple:",tup)

search = input(f"Enter the Search Value:")

if search in tup:
    index = tup.index(search)  #FINDS THE INDEX OF THE SEARCH VALUE USING "index()'
    print(f"{search} is present at {index} index in the Tuple")
else:
    print("INVALID SEARCH VALUE")

# TEST CASES
# Enter number of elements in the tuple:4
# Enter Element 1:25
# Enter Element 2:64
# Enter Element 3:89
# Enter Element 4:48
# Tuple: ('25', '64', '89', '48')
# Enter the Search Value:89
# 89 is present in the Tuple

# Enter number of elements in the tuple:3
# Enter Element 1:19
# Enter Element 2:84
# Enter Element 3:63
# Tuple: ('19', '84', '63')
# Enter the Search Value:94
# INVALID SEARCH VALUE