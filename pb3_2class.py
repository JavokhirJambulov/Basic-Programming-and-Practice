givenString = input("Input any number: ")
strLength = len(givenString)
sumN = 0
for i in range(strLength):
    if givenString[i] != ',':
        sumN += int(givenString[i])
    elif givenString[i] == ',':
        sumN += 0
print(sumN)