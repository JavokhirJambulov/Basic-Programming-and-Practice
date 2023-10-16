
givenString = input("Input any string: ")
print(givenString)
strLength = len(givenString)
a = ''
for i in range(strLength):
    alteredString = givenString[strLength-i -1]
    print(alteredString)
    a += alteredString
print(a)