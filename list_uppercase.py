def create_list():  # FUNCTION TO CREATE LIST
    num = int(input("Enter number of elements in the list: "))
    fruits = []  # BETTER NAMING FOR STRINGS

    for i in range(num):
        value = input(f"Enter fruit {i+1}: ")
        fruits.append(value)   # ADDS ELEMENTS
    return fruits

# Using list comprehension
fruits = create_list()
upper_fruits = [fruit.upper() for fruit in fruits]
print("Uppercase List:", upper_fruits)


# TEST CASES
# Enter number of elements in the list: 3
# Enter fruit 1: banana
# Enter fruit 2: apple
# Enter fruit 3: guava
# Uppercase List: ['BANANA', 'APPLE', 'GUAVA']

# Enter number of elements in the list: 3
# Enter fruit 1: DoctOr StraNGe
# Enter fruit 2: tHaNoS
# Enter fruit 3: iROn MaN
# Uppercase List: ['DOCTOR STRANGE', 'THANOS', 'IRON MAN']