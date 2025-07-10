def create_tuple():
    temp_tup = []
    num = int(input("Enter number of elements:"))
    for i in range(num):
        value = input(f"Enter Element {i+1}:")
        temp_tup.append(value)
    new_tup = temp_tup
    return new_tup

tup = create_tuple()
print("Tuple:",tup)

if all(item == tup[0] for item in tup): #all() checks if all the items in the tuple are identical; returns True or False
    print("All items are identical")
else:
    print("All items are not identical")

# TEST CASES
# Enter number of elements:4
# Enter Element 1:8
# Enter Element 2:8
# Enter Element 3:8
# Enter Element 4:8
# Tuple: ['8', '8', '8', '8']
# All items are identical

# Enter number of elements:3
# Enter Element 1:2
# Enter Element 2:2
# Enter Element 3:1
# Tuple: ['2', '2', '1']
# All items are not identical



