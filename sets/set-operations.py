# iterable objects are lists, dict, sets, string, tuples

# add method is used to append values to the set
# set result is displayed in curly brackets {2, 3}
# don't use comprehension if we have so much of conditional statements

even_numbers = {number for number in range(1, 11) if number % 2 == 0}
# print(even_numbers)

# Matrix

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# writing set comprehension

s = {column for row in matrix for column in row}
# print(s)
# output = {1, 2, 3, 4, 5, 6, 7, 8, 9}

# Sets and frozen Sets challenge

group1 = {"Light Yellow", "Brick Red", "Brick Yellow", "Light Green", "Orange"}
group2 = {"Pink", "Rose", "Light Brown", "Bright Red", "Bright Blue"}
group3 = {"Light Blue", "Light Red", "Medium Red", "Medium Blue", "Light Grey"}

# List all the unique colors of lego blocks of available to you?

# All unique lego blocks using loops

unique_colors = set()
for color in group1:
    unique_colors.add(color)
for color in group2:
    unique_colors.add(color)
for color in group3:
    unique_colors.add(color)

# all unique lego blocks using method

result = group1.union(group2, group3)

output = group1 | group2 | group3

# Find common elements between the sets

# Common lego blocks color using loops

common_elements = set()
for color in group1:
    if (color in group2) and (color in group3):
        common_elements.add(color)

# common lego blocks using method

result1 = group1.intersection(group2, group3)
# result is an empty set

output1 = group1 & group2 & group3

# Determine the difference between two sets

unique_colors1 = set()

for color in group3:
    if (color not in group1) and (color not in group2):
        unique_colors1.add(color)

# using set builtin method. unique elements present in group3 and not in group 1 & 2

result2 = group3.difference(group1, group2)

# Symmetric difference
# List all the colors of lego blocks present in group1 or group2 but
# not in group1 and group2

result3 = group1.symmetric_difference(group2)
# using operator
output3 = group1 ^ group2

# this will give the output as a set. common values present between 2 sets
test1 = group1.intersection(group2)
# this will give a boolean value as result. If the common elements are not present then it will return true
# els it will return False
test2 = group1.isdisjoint(group2)

# Determine a groups is subset of a group
# this will give a boolean value as result. If group1 is subset of group2 then it will return True
# else it will return False
result4 = group1.issubset(group2)
output4 = group1 <= group2


# Determine a groups is superset of a group
# this will give a boolean value as result. If group1 is superset of group2 then it will return True
# else it will return False. Group1 should contains all the values of group2

result5 = group1.issuperset(group2)
output5 = group1 >= group2

