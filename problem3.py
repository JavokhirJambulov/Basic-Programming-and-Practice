givenN = int(input("Input any number: "))
a = ''
temp1 = 0
temp2 = 1
for i in range(0, givenN):
    temp=temp2+temp1
    temp1=temp2
    temp2=temp
    print(temp2)


