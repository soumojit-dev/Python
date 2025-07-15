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
print("Enter elements for the Second set:")
set2 = create_set()
print(f"Second Set : {set2}")

# Symmetric Difference Update
print("Symmetric Difference of First and Second Set : ",set1.symmetric_difference(set2))
set1.symmetric_difference_update(set2)
print("Symmetric Difference Update of First Set w.r.t Second Set: ",set1)
set2.symmetric_difference_update(set1)
print("Symmetric Difference Update of Second Set w.r.t First Set: ",set2)

# Set Differnce Update
print("Difference of First and Second Set : ",set1.difference(set2))
set1.difference_update(set2)
print("Difference Update of First Set w.r.t Second Set: ",set1)
set2.difference_update(set1)
print("Difference Update of Second Set w.r.t First Set: ",set2)

# Intersection Update
print("Enter elements for the Third set:")
set3 = create_set()
print(f"Third Set : {set3}")
print("Enter elements for the Fourth set:")
set4 = create_set()
print(f"Fourth Set : {set4}")
print("Intersection of Third and Fourth Set : ",set3.intersection(set4))
set3.intersection_update(set4)
print("Intersection Update of Third Set w.r.t Fourth Set: ",set3)
set4.intersection_update(set3)
print("Intersection Update of Fourth Set w.r.t Third Set: ",set4)

# TEST CASE
# Enter elements for the First set:
# Enter number of elements in each set:3
# Enter Element 1: apple 
# Enter Element 2: banana
# Enter Element 3: cherry
# First Set : {'banana', 'apple', 'cherry'}
# Enter elements for the Second set:
# Enter number of elements in each set:3
# Enter Element 1: kiwi
# Enter Element 2: banana
# Enter Element 3: cherry
# Second Set : {'banana', 'cherry', 'kiwi'}
# Symmetric Difference of First and Second Set :  {'apple', 'kiwi'}
# Symmetric Difference Update of First Set w.r.t Second Set:  {'apple', 'kiwi'}
# Symmetric Difference Update of Second Set w.r.t First Set:  {'banana', 'apple', 'cherry'}
# Difference of First and Second Set :  {'kiwi'}
# Difference Update of First Set w.r.t Second Set:  {'kiwi'}
# Difference Update of Second Set w.r.t First Set:  {'banana', 'apple', 'cherry'}
# Enter elements for the Third set:
# Enter number of elements in each set:3
# Enter Element 1: mango
# Enter Element 2: guava
# Enter Element 3: grapes
# Third Set : {'mango', 'guava', 'grapes'}
# Enter elements for the Fourth set:
# Enter number of elements in each set:3
# Enter Element 1: papaya
# Enter Element 2: guava
# Enter Element 3: grapes
# Fourth Set : {'papaya', 'guava', 'grapes'}
# Intersection of Third and Fourth Set :  {'guava', 'grapes'}
# Intersection Update of Third Set w.r.t Fourth Set:  {'guava', 'grapes'}
# Intersection Update of Fourth Set w.r.t Third Set:  {'guava', 'grapes'}



