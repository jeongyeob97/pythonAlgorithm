# from collections import defaultdict
#
# node, answer = defaultdict(int), defaultdict(int)
# node[1] = 10
#
# repeat = int(input())
#
# for i in range(repeat-1):
#
#     num1, num2 = map(int,input().split())
#
#     if node[num1] == 0:
#         node[num1] = 10
#         answer[num1] = num2
#     else:
#         node[num2] = 10
#         answer[num2] = num1
#
# for i in range(2, repeat+1):
#     print(answer[i])

# num = int(input())
# answer = [False] * (num+1)
# answer[1] = 1
# for i in range(num-1):
#     num1, num2 = map(int,input().split())
#     if answer[num1]:
#         answer[num2] = num1
#     else:
#         answer[num1] = num2
# for i in range(2,num+1):
#     print(answer[i])

import sys
from collections import defaultdict, deque

num = int(sys.stdin.readline())
answer = [False] * (num+1)
data = defaultdict(list)

for i in range(num-1):
    x,y = map(int,sys.stdin.readline().split())
    data[x].append(y)
    data[y].append(x)

list1 = deque([1])

while list1:
    number = list1.popleft()
    for i in data[number]:
        if answer[i] == False:
            list1.append(i)
            answer[i] = number

for i in range(2,num+1):
    print(answer[i])








