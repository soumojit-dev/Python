#unpacking into 3 variable using * operator
print("----FIRST TUPLE----")
tup = ("apple", "banana", "guava", "grapes")
(item1, item2, *item3) = tup  
print(item1)
print(item2)
print(item3)
#unpacking into 2 variable using * operator
print("----SECOND TUPLE----")
tup_A = ("apple", "banana", "guava", "grapes")
(ele1, *ele2) = tup_A
print(ele1)
print(ele2)

# TEST CASEE
# ----FIRST TUPLE----
# apple
# banana
# ['guava', 'grapes']
# ----SECOND TUPLE----
# apple
# ['banana', 'guava', 'grapes']
