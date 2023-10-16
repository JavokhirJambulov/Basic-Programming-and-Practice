a = int(input("Input the number of keys in dict: "))
dict1 = {}
dict2 = {}
dict3 = {}

def dictCreationFunc(b):
    dictN = {}
    print("Input the values for the new Dictionary:")
    for i in range(b):

        key = input("Input the key: ")
        value = int(input("Input the values: "))
        dictN.update({key: value})
    return dictN

def dictMergeFunc(dictA,dictB):
    dictMerge = {}
    for k, v in dictA.items():
        dictMerge.update({k:v+dictB.get(k,0)})

    for k1, v1 in dictB.items():
        if k1 not in dictMerge:
            dictMerge.update({k1: v1})
    return dictMerge


dict1 = dictCreationFunc(a)
dict2 = dictCreationFunc(a)
dict3 = dictMergeFunc(dict1,dict2)

print(dict1)
print(dict2)
print(dict3)