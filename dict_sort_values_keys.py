def create_dict(n):
    dic = {}
    for i in range(n):
        key = input(f"Enter Key {i+1}: ")
        value = input(f"Enter Value for {key}: ")
        dic[key] = value
    return dic

n1 = int(input("Enter number of entries for the Dictionary: "))
dict1 = create_dict(n1)
print(f"Dictionary : {dict1}")

# sorting by value
sort_value = dict(sorted(dict1.items(), key=lambda x: x[1]))
print(f"After Sorting by Value, the Dictionary: {sort_value}")

# sorting by keys
sort_keys = dict(sorted(dict1.items(), key=lambda x: x[0]))
print(f"After Sorting by Keys, the Dictionary: {sort_keys}")

# TEST CASES
# Enter number of entries for the Dictionary: 3
# Enter Key 1: x
# Enter Value for x: 56
# Enter Key 2: a
# Enter Value for a: 78
# Enter Key 3: p
# Enter Value for p: 43
# Dictionary : {'x': '56', 'a': '78', 'p': '43'}
# After Sorting by Value, the Dictionary: {'p': '43', 'x': '56', 'a': '78'}
# After Sorting by Keys, the Dictionary: {'a': '78', 'p': '43', 'x': '56'}

# Enter number of entries for the Dictionary: 3
# Enter Key 1: 1.
# Enter Value for 1.: grapes
# Enter Key 2: 2.
# Enter Value for 2.: apple
# Enter Key 3: 3.
# Enter Value for 3.: kiwi
# Dictionary : {'1.': 'grapes', '2.': 'apple', '3.': 'kiwi'}
# After Sorting by Value, the Dictionary: {'2.': 'apple', '1.': 'grapes', '3.': 'kiwi'} => sorted based on alphabetical order a > g > k
# After Sorting by Keys, the Dictionary: {'1.': 'grapes', '2.': 'apple', '3.': 'kiwi'} => sorted based on numeric order (ascending order)