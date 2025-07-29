try:
    num = int(input("Enter a number: "))
    a = [6,2,8]
    print(a[num])
except ValueError:
    print("Entered input is not an integer!")
except IndexError:
    print("Index out of range!")

# TEST CASES
# Enter a number: 1
# 2

# Enter a number: 5
# Index out of range!

# Enter a number: Soumo
# Entered input is not an integer!