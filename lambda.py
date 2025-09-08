numList = [(5, 4), (10, 7), (500, 3), (732, 46), (88, 1)]
sortedList = sorted(numList, key=lambda x: x[1])
print(sortedList)

nestedList = [1, [[[2], 3, 4], 5], 6]
unNestedList = []
while len(nestedList) > 0:
    for i in range(len(nestedList)):
        if not isinstance(nestedList[i - 1], list):
            unNestedList.append(nestedList.pop(i - 1))
        if len(nestedList) == 1:
            nestedList = nestedList[0]

print(unNestedList)