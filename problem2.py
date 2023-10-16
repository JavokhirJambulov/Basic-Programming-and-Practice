givenString = input("Input any string: ")
strLength = len(givenString)
isItPalindrome = 0
for i in range(strLength):
    if givenString[i] == givenString[strLength-1-i]:
        isItPalindrome = 1
    else:
        isItPalindrome = 0

if isItPalindrome == 1:
    print("It is palindrome")
else:
    print("It is not palindrome")