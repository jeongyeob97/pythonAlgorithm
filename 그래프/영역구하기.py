import sys
from collections import deque
M,N,K = map(int,sys.stdin.readline().strip().split())

graph = [[False]*N for _ in range(M)]
answer = []

for _ in range(K):
    y1, x1, y2, x2 = map(int,sys.stdin.readline().strip().split())
    for i in range(x1,x2):
        for j in range(y1,y2):
            graph[i][j] = True

def bfs(point, m, n):
    deque_list = deque(point)

    x = [1,-1,0,0]
    y = [0,0,1,-1]
    cnt = 0
    graph[point[0][0]][point[0][1]] = True

    while deque_list:
        coor = deque_list.popleft()

        cnt+=1

        for i in range(4):
           if (0 <= coor[0] + x[i] < m) and (0 <= coor[1] + y[i] < n) and (not graph[coor[0]+x[i]][coor[1]+y[i]]):
                graph[coor[0] + x[i]][coor[1] +y[i]] = True
                deque_list.append([coor[0]+x[i], coor[1]+y[i]])

    return cnt

for i in range(M):
    for j in range(N):
        if graph[i][j] == False:
            answer.append(bfs([[i,j]],M,N))

print(*sorted(answer))
