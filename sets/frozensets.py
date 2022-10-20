# Accessing values from set
# sets are unordered data types. So we won't be able to access the values using index values.

s = {"raju", "rani", "naveen", "uma"}
# TypeError: 'set' object is not subscriptable
# print(s[0])

# this is a built-in function which will assign some indexes to the values.
for key, value in enumerate(s):
    print(key, value)

# find the largest number in the set
s1 = {1, 2, 3, 0.5, 500, 300}
# we have to convert it into ordered data object
ordered = list(s1)
largest = ordered[0]

for number in ordered:
    if number > largest:
        largest = number

# Writing the same using built-in method

largest1 = max(s1)

# smallest value

smallest = min(s1)

# Sort the set elements
# sorted accepts iterable as a parameter

marks = {85, 50, 80, 70, 75, 60.5}
# this will sort the data in descending order
sorted_marks = sorted(marks)
# Below will print the data in ascending order
ascend = sorted(marks, reverse=True)

# Based on the length of each word.
strings = {"javascript", "python", "flask", "go"}
sorted_strings = sorted(strings, key=len, reverse=True)

# Sorting a set containing mixed data types

s2 = {1, 2, "hello"}
# result = sorted(s2)

# We can have lists or sets with multiple data types. but we won't be able to perform many operations
list1 = [1, 2, "hello"]

# Sum of all the elements

sum1 = {10, 20, 30, 40, 50, 60}
total = 0
for num in sum1:
    total += num

def sum_with_using_builtin():
    s4 = {10, 20, 30, 40, 50, 60}
    total = sum(s4)
    return  total

# Frozensets
# it is immutable

x = frozenset([1, 2, 3])
print(f"frozen set is {x}")

print(dir(frozenset({1, 2, 3})))

for method in dir(frozenset({1, 2, 3})):
    if not method.startswith('__'):
        print(method)
# any method that starts with __ and endswith __ called as magic methods

for builtin in dir(set()):
    if not builtin.startswith('__'):
        print(builtin)
# for converting a mutable object into immutable object, we need frozenset

set1 = {1, 2, 3, 4, 5, 6}
list2 = [1, 2, 3, 4, 5, 6]
dict1 = {"first_name": "raju", "last_name": "naveen", "full_name": "naveen raju"}

frozen_set = frozenset(set1)
frozen_list = frozenset(list2)
frozen_dict = frozenset(dict1)

dict3 = {frozenset({1, 2, 3}): "london"}
print(dict3)
# frozenset can be used as a key in the dictionary, because it is immutable. We can't use set, list as keys. they are
# mutable objects

# Create a frozenset

x = frozenset()
x.add(1) # it is not possible

x = frozenset({1, 2, 3, "hello"})
