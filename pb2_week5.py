list1 = []
dict1 = {}

a = int(input("Input the number of keys in dict: "))
thresholdValue = int(input("Input threshold value: "))


def dict_creation(a):
    for i in range(a):
        b = int(input("values for dict: "))
        dict1.update({'item' + str(i): b})


def list_creation():
    for i in dict1.values():
        if i > thresholdValue:
            list1.append(i)


dict_creation(a)
list_creation()
print(dict1)
print(list1)
