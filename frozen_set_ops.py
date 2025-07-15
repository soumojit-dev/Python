def create_frozen_set():
    n = int(input("Enter number of elements: "))
    temp_set = set()
    for i in range(n):
        value = input(f"Enter Element {i+1}: ")
        temp_set.add(value)
    return frozenset(temp_set)

#UNLIKE SETS, FROZEN SETS ARE IMMUTABLE i.e., CANNOT BE ALTERED

print("FROZEN SET 1: ")
frozen1 = create_frozen_set()
print("Frozen Set 1 :", frozen1)

print("FROZEN SET 2: ")
frozen2 = create_frozen_set()
print("Frozen Set 2 :", frozen2)

# UNION OF FROZEN SETS
print("Union of Frozen Set 1 & 2 : ", frozen1.union(frozen2))

#INTERSECTION OF FROZEN SETS
print("Intersection of Frozen Set 1 & 2 : ", frozen1.intersection(frozen2))

#DIFFERENCE OF FROZEN SETS
print("Difference of Frozen Set 1 & 2 : ", frozen1.difference(frozen2))

#SYMMETRIC DIFFERENCE OF FROZEN SETS
print("Symmetric Difference of Frozen Set 1 & 2 : ", frozen1.symmetric_difference(frozen2))

# TEST CASE
# FROZEN SET 1: 
# Enter number of elements: 3
# Enter Element 1: apple
# Enter Element 2: banana
# Enter Element 3: cherry
# Frozen Set 1 : frozenset({'apple', 'banana', 'cherry'})
# FROZEN SET 2:
# Enter number of elements: 3
# Enter Element 1: papaya
# Enter Element 2: banana
# Enter Element 3: cherry
# Frozen Set 2 : frozenset({'papaya', 'banana', 'cherry'})
# Union of Frozen Set 1 & 2 :  frozenset({'papaya', 'apple', 'banana', 'cherry'})
# Intersection of Frozen Set 1 & 2 :  frozenset({'banana', 'cherry'})
# Difference of Frozen Set 1 & 2 :  frozenset({'apple'})
# Symmetric Difference of Frozen Set 1 & 2 :  frozenset({'papaya', 'apple'})

