from collections import deque

n, m = map(int, input().split())
start = deque()
graph = []

for i in range(m):
    temp = input()
    graph.append(list(temp))
    for j in range(n):
        if temp[j] == "c":
            start.append((i, j))

answer = [[float('inf')]*n for i in range(m)]

for i in start:
    x,y = i
    answer[x][y] = 0

while start:
    x,y = start.popleft()

    if x+1 < m:
        if (answer[x+1][y] > answer[x][y]) and (graph[x+1][y] != "x"):
            answer[x+1][y] = answer[x][y]
            start.append((x+1,y))
    if y+1 < n:
        if (answer[x][y+1] > answer[x][y]+1) and (graph[x][y+1] != "x"):
            answer[x][y+1] = answer[x][y]+1
            start.append((x,y+1))
    if y-1 >= 0:
        if (answer[x][y-1] > answer[x][y]+1) and (graph[x][y-1] != "x"):
            answer[x][y-1] = answer[x][y] + 1
            start.append((x,y-1))

minimum = min(answer[-1])
if minimum == float('inf'):
    print(-1)
else:
    print(minimum)