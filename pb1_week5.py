# a = int(input("Input the number of lists: "))

list1 = []
list2 = []
dict1 = {}


def listCreationFunction():
    print("Values for list1")
    for i in range(0, 4):
        num = int(input("Input the values: "))
        list1.append(num)
    print("Values for list2")
    for m in range(0, 4):
        num = int(input("Input the values : "))
        list2.append(num)


def dictCreationFunc():
    for i in range(0, 4):
        for j in range(0, 4):
            if list1[i] == list2[j]:
                dict1.update({list1[i]: list1[i] * 2})


listCreationFunction()
dictCreationFunc()
print(list1, list2)
print(dict1)
