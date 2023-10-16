list1 = []
list2 = []
dict1 = {}

targetSum = int(input("Input the target sum: "))


def listCreationFunction():
    print("Values for list")
    for i in range(0, 5):
        num = int(input("Input the values: "))
        list1.append(num)


def dictCreationFunc():
    for i in range(0, 5):
        for j in range(i+1, 5):
            if list1[i] + list1[j] == targetSum:
                dict1.update({list1[i]: list1[j]})


listCreationFunction()
dictCreationFunc()
print(list1)
print(dict1)
