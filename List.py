numberList = [1,2,3,4,5,6]
print(numberList[0])
print(numberList[-3])

## Loop
nameList = ["A", "B", "C"]
for n in nameList:
    print(n)

## append
numberList.append(7)
print(numberList[6])

## List Comprehension
squares = [n * n for n in numberList]
print(squares)