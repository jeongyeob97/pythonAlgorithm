def find(available, graph, n, m):
    x_list = [0,0,-1,1]
    y_list = [1,-1,0,0]
    while available:
      x,y = available.pop()
      graph[x][y] = 0
      for i in range(4):
        temp_x, temp_y = x + x_list[i], y + y_list[i]
        if (0 <= temp_x < n) and (0 <= temp_y < m) and (graph[temp_x][temp_y] == 1):
          if temp_x == n-1:
            return 1
          available.append((temp_x, temp_y))
    return -1


import sys
input = sys.stdin.readline
n,m = map(int,input().split())

available = []
graph = []

for i in range(n):
    temp = list(map(int,list(input().strip())))
    if i == 0:
        for j in range(len(temp)):
            if temp[j] == 1:
                available.append((i,j))
    graph.append(temp)

print(find(available,graph,n,m))