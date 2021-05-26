import sys
from collections import deque

input = sys.stdin.readline
n,m = map(int,input().split())

available = deque()
graph = []
answer = []

for i in range(n):
    answer.append([float('inf')] * m)

for i in range(n):
    temp = list(map(int,list(input().strip())))
    if i == 0:
        for j in range(len(temp)):
            if temp[j] == 1:
                available.append((i,j))
                answer[i][j] = 1
    graph.append(temp)

x_list = [0, 0, -1, 1]
y_list = [1, -1, 0, 0]

while available:
    x, y = available.popleft()

    for i in range(4):
        if (0 <= x + x_list[i] < len(graph)) and (0 <= y + y_list[i] < len(graph[0])) and graph[x + x_list[i]][y + y_list[i]] == 1 and answer[x + x_list[i]][y + y_list[i]] > answer[x][y] + 1:
            answer[x + x_list[i]][y + y_list[i]] = answer[x][y] + 1
            available.append((x+x_list[i], y+y_list[i]))

minimum = min(answer[-1])
print([minimum, -1][minimum == float('inf')])