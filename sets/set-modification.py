# Modifying sets

s1 = set()
s1.add('import')
s1.add('export')

numbers = {1, 2, 3, 4, 5}
numbers.add(10)

# Add same element twice

s2 = {1, 2, 3, 5}
s2.add(10)
s2.add(10)
# 10 will be added only once

# add elements by using loop
x = set()
for i in range(1, 1001):
    x.add(i)


# Add all elements from one set to another

def add_using_loops(s1, s2):
    for i in s2:
        s1.add(i)
    return s1

# using a builtin method
def using_builtin(s3, s4):
    # builtin method does not rerun anything. It just updates inplace
    s3.update(s4)
    return s3


a1 = {2, 4, 6, 8, 10, 12}
a2 = {1, 3, 5, 7, 9, 11}

b1 = add_using_loops(a1, a2)
b2 = using_builtin(a1, a2)

# Remove elements from a set

def remove_without_using_loops(numbers):
    print("before", numbers)
    numbers.remove(30)
    print("after", numbers)
    # remove method will not return anything
    result = numbers.remove(20)
    print("value returned by remove method after removing an element", result)

def remove_using_loops(numbers):
    print("Value of set before removing the element from it ", numbers)
    # we cannot change the size of a set using loop
    diplicate_set = numbers.copy()
    for number in diplicate_set:
        if number%3==0:
            numbers.remove(number)
    print("Value of set after removing the element from it ", numbers)


def remove_number_does_not_exist(numbers):
    # we will get key error when the element does not exists in the set.
    numbers.remove(100)

numbers = {10, 20, 30, 40, 50}
remove_without_using_loops(numbers)
remove_using_loops(numbers)
remove_number_does_not_exist(numbers)

# We can use discard also to remove an element from the set
countries = {"USA", "Canada", "UK", "India"}
countries.discard("UK")

# Difference between discard and remove
# Discard method didn't raise any ERROR, if the value is not present in the set

# using pop method with Set and List
# As set is a unordered data set, pop will remove random element, however in List it will remove last element
# list.pop(), set.pop()

# remove all elements from set
s1 = {1, 2, 3, 4}
s1.clear()
