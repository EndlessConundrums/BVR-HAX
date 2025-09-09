length = 10
numOne = 1
numTwo = 0
for i in range(length):
    temp = numOne
    numOne += numTwo
    numTwo = temp
    print(numOne)

def fibonacci(length, numOne, numTwo):
    length -= 1
    temp = numOne
    numOne += numTwo
    numTwo = temp
    print(numOne)
    if length > 0:
        fibonacci(length, numOne, numTwo)

fibonacci(10, 1, 0)