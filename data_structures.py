# strings
# In strings we can use (" ") or (' ') quotations.
# we can't modify the string character. It is immutable.
# string methods:
str = "  python  "
print(str.strip())
str = "python"
print(str.upper())
print(str.lower())
print(str.split(" "))

# Lists
# It is an order of collection of items.
# print list items using for loops:
num = [10, 20, 30, 40, 50]
for x in num:
    print(x)
# list methods:
num = [1, 2, 3, 4]
num.append(5), print(num)
num.insert(0, 10), print(num)
num.remove(10), print(num)
num.clear(), print(num)

# Tuples
# It is a sequence of immutable python objects.
# similar list but it's can't be changed once its assigned.

# modifying tuples elements:
# remove, replace, append, del by using these values we can't modify th tuples.
# Tuples methods:
# finding the length:
tuple = (1, 2, 3, 4)
print(len(tuple))
# Item count:
tuple = (1, 2, 1, 4)
print(tuple.count(1))
# index of item:
tuple = (1, 2, 1, 4)
print(tuple.index(4))

# Dictionary
# It is an unordered collection of items. Instead of just values we will have key value pairs.
# modifications:
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
# change value
dict["Name"] = 'ziya'
print(dict)
# adding items
dict["Gender"] = 'Female'
print(dict)
# Remove items
Gender = dict.pop("Gender")
print(Gender)
print(dict)
# empty items
dict.clear()
print(dict)
# dictionary methods
dictionary = {"Name": "ziya"}
copy = dictionary.copy()
print(copy)

# sets
# It is an unordered collection of items with duplicates.
# modifying items
fruits = {"apple", "banana", "cherry"}
# add item
fruits.add('orange'), print(fruits)
# remove item
fruits.remove('orange'), print(fruits)
# discard item
fruits.discard("apple"), print(fruits)
# empty set
fruits.clear(), print(fruits)
