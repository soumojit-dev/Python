def create_tuple(): #FUNCTION FOR CREATING A TUPLE
    num = int(input("Enter number of elements:"))
    temp_tup =[]   #EMPTY LIST
    for i in range(num):
        value = input(f"Enter Element {i+1}:")
        temp_tup.append(value)   #ADDS VALUE TO THE LIST
    new_tup = tuple(temp_tup)    #LIST -> TUPLE CONVERSION
    return new_tup

tup = create_tuple()
print("Original Tuple:",tup)

rev_tup = tup[::-1]   #TUPLE REVERSING LOGIC
      #OR
# l = len(tup)
# rev_tup = tup[l::-1] => [start:end:jump]   #ALTERNATE TUPLE REVERSING LOGIC
print("Reversed Tuple:",rev_tup)

# TEST CASE
# Enter number of elements:4
# Enter Element 1:28
# Enter Element 2:DUBAI
# Enter Element 3:65
# Enter Element 4:Vantara
# Original Tuple: ('28', 'DUBAI', '65', 'Vantara')
# Reversed Tuple: ('Vantara', '65', 'DUBAI', '28')