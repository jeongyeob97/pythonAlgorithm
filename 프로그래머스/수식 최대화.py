from collections import defaultdict
from itertools import permutations
def solution(expression):
    answer = 0
    temp_operation = ["+", "-", "*"]
    operationDict = {
        "+": (lambda x,y: x+y),
        "-": (lambda x,y: x-y),
        "*": (lambda x,y: x*y)
    }

    expressionList, operationList = stringToList(expression, temp_operation)

    priorityList = permutations(operationList, len(operationList))

    for priority in priorityList:
        answer = max(answer,cal(priority, expressionList, operationDict))
        # cal(priority, expressionList, operationDict)
    return answer
def cal(priority, expressionList, operationDict):
    expressionListCopy = expressionList[:]
    for operation in priority:
        index = 1
        while True:
            if index >= len(expressionListCopy):
                break
            if expressionListCopy[index] == operation:
                num = operationDict[operation](expressionListCopy[index-1], expressionListCopy[index+1])
                expressionListCopy[index-1: index+2] = [num]
            else:
                index+=2
    return(abs(expressionListCopy[0]))


def stringToList(expression, temp_operation):
    number = ""
    operation = defaultdict(int)
    expressionList = []
    operationSet = set()

    for i in temp_operation:
        operation[i] = 1

    for i in expression:
        if operation[i] == 1:
            expressionList.append(int(number))
            expressionList.append(i)
            operationSet.add(i)
            number = ""
            continue

        number += i
    expressionList.append(int(number))

    return expressionList, list(operationSet)


# solution("100-200*300-500+20")
print(solution("100-200*300-500+20"))
print(solution("50*6-3*2"))