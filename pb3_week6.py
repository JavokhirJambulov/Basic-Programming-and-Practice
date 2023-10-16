list1 = []
dict1 = {}

listSize = int(input("Input the list size: "))


def listCreationFunction():
    print("Values for list")
    for i in range(listSize):
        num = int(input("Input the values: "))
        list1.append(num)


def dictCreationFunc():
    for num in list1:
        if num in dict1:
            dict1[num] += 1
        else:
            dict1[num] = 1


listCreationFunction()
dictCreationFunc()
print(list1)
print(dict1)
