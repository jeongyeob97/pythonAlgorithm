
from itertools import combinations
from collections import deque

n, m = map(int,input().split())

available = []
virus = []
graph = []
for i in range(n):
    temp = list(map(int,input().split()))
    for j in range(len(temp)):
        if temp[j] == 0:
            available.append((i,j))
        elif temp[j] == 2:
            virus.append((i,j))

    graph.append(temp)

maximum = 0

cases = list(combinations(available,3))

x_list = [0,0,1,-1]
y_list = [1,-1,0,0]

for case in cases:
    callback = []
    deque_virus = deque(virus)
    cnt = 0

    for x,y in case:
        graph[x][y] = 1

    while deque_virus:
        origin_x, origin_y = deque_virus.popleft()

        if len(available) - cnt < maximum:
            break
        for i in range(4):

            temp_x =origin_x + x_list[i]
            temp_y = origin_y + y_list[i]

            if (0<=temp_x<len(graph)) and (0<=temp_y<len(graph[0])) and (graph[temp_x][temp_y] == 0):
                cnt += 1
                graph[temp_x][temp_y] = 2
                callback.append((temp_x,temp_y))
                deque_virus.append((temp_x,temp_y))

    for x,y in case:
        graph[x][y] = 0
    for temp_x, temp_y in callback:
        graph[temp_x][temp_y] = 0
    maximum = max(len(available)-cnt,maximum)

print(maximum-3)