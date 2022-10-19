def without_set_membership(numbers, search_element):
    for number in numbers:
        if number == 4:
            print("true")

def set_membership(numbers, search_element):
    # in: returns true if the object exists in set else returns false
    result = search_element in numbers
    print(f"Result of using in operator is {result}")

    # not in: returns true if the object does not exists in set else returns false
    output = search_element not in numbers
    print(f"Result of using not in operator is {output}")


def list_membership(numbers, search_element):
    result = search_element in list(numbers)
    print(f"Result of using  in operator list is {result}")

key = 4
even_numbers = {2, 4, 6, 8, 10, 12}
without_set_membership(even_numbers, key)
set_membership(even_numbers, key)
list_membership(even_numbers, key)

"""All operations are executed within short time. if the object data is huge, using sets are faster
compared to other data structures. Because set contains only unique values"""
