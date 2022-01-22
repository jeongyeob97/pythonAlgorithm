from collections import defaultdict
from copy import deepcopy
import sys

def bfs(x,y):
    answer = 1
    temp = [[0,0,-1,1], [1,-1,0,0]]

    q = set([(x,y,graph[x][y])])

    while q:
        x1,y1,ans = q.pop()

        for i in range(4):
            tX = x1 + temp[0][i]
            tY = y1 + temp[1][i]

            if 0 <= tX < n and 0 <= tY < m and graph[tX][tY] not in ans:
                q.add((tX,tY, ans + graph[tX][tY]))
                answer = max(answer, len(ans) + 1)
    return answer




input = sys.stdin.readline

n,m = map(int,input().split())

graph = []
for i in range(n):
    graph.append(list(input().strip()))
print(bfs(0,0))

