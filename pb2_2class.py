#a, e, i, o, u
givenString = input("Input any string: ")
strLength = len(givenString)
vowelN = 0
for i in range(strLength):
    if givenString[i] == 'a' or givenString[i] == 'e' or givenString[i] == 'i' or givenString[i] == 'o' or givenString[i] == 'u':
        vowelN +=1

print("There are " + str(vowelN) + " vowels in given string " + givenString)
