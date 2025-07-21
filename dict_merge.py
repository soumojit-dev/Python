def create_dict(n):
    dic = {}
    for i in range(n):
        key = input(f"Enter Key {i+1}: ")
        value = input(f"Enter value of {key}: ")
        dic[key] = value
    return dic

n1 = int(input("Enter number of entries in Dict 1: "))
dict1 = create_dict(n1)
print(f"Dictionary 1: {dict1}")

n2 = int(input("Enter number of entries in Dict 2: "))
dict2 = create_dict(n2)
print(f"Dictionary 2: {dict2}")

merged = {}
merged = dict.copy(dict1)

merged.update(dict2)
print(f"After Merging Dictionary 1 & 2: {merged}")

# TEST CASE
# Enter number of entries in Dict 1: 2
# Enter Key 1: a
# Enter value of a: 1
# Enter Key 2: b
# Enter value of b: 2
# Dictionary 1: {'a': '1', 'b': '2'}
# Enter number of entries in Dict 2: 3
# Enter Key 1: c
# Enter value of c: 3
# Enter Key 2: d
# Enter value of d: 4
# Enter Key 3: e
# Enter value of e: 5
# Dictionary 2: {'c': '3', 'd': '4', 'e': '5'}
# After Merging Dictionary 1 & 2: {'a': '1', 'b': '2', 'c': '3', 'd': '4', 'e': '5'}

