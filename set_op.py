def create_set():  #function to create set
    n = int(input("Enter number of elements in each set:"))
    s = set()  #Empty set
    for i in range(n):
        value = input(f"Enter Element {i+1}: ")
        s.add(value)
    return s

print("Enter elements for the First set:")
set1 = create_set()
print(f"First Set : {set1}")
print("Enter elements for the Second set (same inputs):")
set2 = create_set()
print(f"Second Set : {set2}")
print("Enter the elements for the Third set:")
set3 = create_set()
print(f"Third Set : {set3}")

# Common Elements in Three Sets
com = set1.intersection(set2) | set1.intersection(set3) | set2.intersection(set3)
print("Common Elements in Three Sets -> Set1, Set2, Set3 => ",com)

# Common Elements in Two Sets 
common = set1.intersection(set2)  #Also using Intersection Operator : set1 & set2
print("The Common elements in both sets are: ", common)

# Check Subset Relationship
print("Is set1 a subset of set2?", set1.issubset(set2))
print("Is set2 a subset of set1?", set2.issubset(set1))

# Set Difference and Symmetric Difference
print("The Difference of set1 and set2 is: ", set1.difference(set2)) #Also using Difference Operator : set1 - set2
print("The Symmetric Difference of set1 and set2 is: ", set1.symmetric_difference(set2)) #Also using Symmetric Difference Operator : set1^set2

# Set to List and List to Set Conversion
list1 = set1
print("Set1 to List Conversion => ",list(list1))
print("List to Set1 Conversion => ",set(list1))

# Union of Sets
print("The Union of set1 and set2 is: ", set1.union(set2)) #Also using Union Operator : set1|set2

# Unique Words in a Sentence
sent = input("Enter a sentence: ")
words = sent.split()
unique_wrds = set(words)
print("Unique Words : ", unique_wrds)

# # TEST CASE
# Enter elements for the First set:
# Enter number of elements in each set:3
# Enter Element 1: apple
# Enter Element 2: banana
# Enter Element 3: cherry
# First Set : {'apple', 'banana', 'cherry'}       
# Enter elements for the Second set (same inputs):
# Enter number of elements in each set:3
# Enter Element 1: banana
# Enter Element 2: cherry
# Enter Element 3: mango
# Second Set : {'mango', 'banana', 'cherry'}
# Enter the elements for the Third set:
# Enter number of elements in each set:3
# Enter Element 1: cherry 
# Enter Element 2: banana
# Enter Element 3: papaya
# Third Set : {'banana', 'papaya', 'cherry '}
# Common Elements in Three Sets -> Set1, Set2, Set3 =>  {'banana', 'cherry'}
# The Common elements in both sets are:  {'banana', 'cherry'}
# Is set1 a subset of set2? False
# Is set2 a subset of set1? False
# The Difference of set1 and set2 is:  {'apple'}
# The Symmetric Difference of set1 and set2 is:  {'mango', 'apple'}
# Set1 to List Conversion =>  ['apple', 'banana', 'cherry']
# List to Set1 Conversion =>  {'apple', 'banana', 'cherry'}
# The Union of set1 and set2 is:  {'mango', 'apple', 'banana', 'cherry'}
# Enter a sentence: Python is easy and Python is powerful
# Unique Words :  {'easy', 'and', 'Python', 'is', 'powerful'}
