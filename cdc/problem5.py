# problem5
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20

startingNum = 20
originalArray = []

for x in range(1, startingNum + 1):
    originalArray.append(x)

def getMultiples(num):
    finalDict = {}
    for x in range(2, num + 1):
        while (num % x == 0 and num > 1):
            num /=x
            if x in finalDict:
                finalDict[x] += 1
            else:
                finalDict[x] = 1
    return finalDict

def lowestMultiple(array):
    multiple = {}
    for x in array:
        returnedMultiples = getMultiples(x)
        for y in returnedMultiples:
            if (y in multiple and returnedMultiples[y] >= multiple[y]) or (y not in multiple):
                multiple[y] = returnedMultiples[y]
    return multiple

final = lowestMultiple(originalArray)

multiply = 1
for x in final:
    print("x = ", x)
    for y in range(1, final[x] + 1):
        print('final = ', y)
        multiply *= x
