list1 = ['hello', 'this', 'is', 'BTechGeeks']
list2 = ['this', 'is', 'BTechGeeks', 'hello']

# Set will convert the list into sorted sequence set of data items without taking the order of elements into
# consideration.
a = set(list1)
print(a)
b = set(list2)
print(b)

if a == b:
    print("Both lists are same")
else:
    print("Both lists are not equal")