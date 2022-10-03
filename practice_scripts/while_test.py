import time
list1 = []

count = 50

while len(list1) != count:
    print(list1)
    print(len(list1))
    time.sleep(5)
    if len(list1) == count:
        print("All logical switches are fetched")
    else:
        for i in range(0, 10):
            list1.append(i)
        print("All logical switches are not fetched")