import sys
sys.stdin.readline()
list1 = sys.stdin.readline().strip()
operandDict = {"+" : lambda x,y: x+y, "-": lambda x,y: x-y, "*": lambda x,y: x*y}
num, operand = [], []
for i in range(len(list1)):
    if i%2 == 0:
        num.append(int(list1[i]))
    else:
        operand.append(list1[i])

def findMax(number, operand, nested):
    maximum = 0
    if len(operand) == 1:
        return operandDict[operand[0]](number[0],number[1])
    for i in range(len(operand)):
        if nested == number[i]:
            continue
        result = operandDict[operand[i]](number[i],number[i+1])
        tempNum = number[:i] + [result] + number[i+2:]
        tempOperand = operand[:i] + operand[i+1:]
        maximum = max(maximum, findMax(tempNum, tempOperand,result))
    return maximum

print(findMax(num,operand,float('inf')))

