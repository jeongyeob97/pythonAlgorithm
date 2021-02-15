def add_paren(text_list, idx, length):
    if idx >= length-1:
        return calculate(text_list)
    max_list = []
    if text_list[idx] == "_":
        temp1 = deepcopy(text_list)
        if idx + 6 < length:
            temp1[idx]="("
            temp1[idx+6]=")"
            max_list.append(add_paren(temp1, idx+8, length))
        if idx+4 < length:
            max_list.append(add_paren(text_list,idx+4, length))
        else:
            temp = length-idx
            max_list.append(add_paren(text_list, idx+temp, length))
    return max(max_list)

def calculate(expression):
    answer, idx = float('inf'), 0

    while idx < len(expression):
        if answer == float("inf"):
            if expression[idx] == "_":
                answer = int(expression[idx+1])
                idx += 3
            else:
                answer = cal2(expression,idx)
                idx += 7
        else:
            if expression[idx+1] == "_":
                answer = operand_dict[expression[idx]](answer,int(expression[idx+2]))
                idx += 4
            else:
                answer = operand_dict[expression[idx]](answer,cal2(expression,idx+1))
                idx += 8

    return answer

def cal2(expression,idx):
    return operand_dict[expression[idx+3]](int(expression[idx+1]), int(expression[idx+5]))

import sys
from copy import deepcopy

n = int(sys.stdin.readline().strip())

str1 = "_"
for i in sys.stdin.readline().strip():
    str1 += i+"_"
list1 = list(str1)

operand_dict = {"+": lambda x,y: x+y, "*": lambda x,y: x*y, "-": lambda x,y: x-y}


print(add_paren(list1,0,len(list1)))

