givenN = int(input("Input any number: "))


# factorialN = 1
# for i in range(1, givenN+1):
#     factorialN *= i
#
# print(factorialN)

def recursive_factorial(n):
    if n == 1:
        return n
    else:
        return n * recursive_factorial(n - 1)


print(recursive_factorial(givenN))
