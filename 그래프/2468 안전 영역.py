def dfs(x, y, num, elevation_graph, visited_graph):
    visited_graph[x][y] = True
    if x-1 >= 0:
        if (elevation[x-1][y] > num) & (visited_graph[x-1][y] == False):
            dfs(x-1, y, num, elevation_graph, visited_graph)
    if y-1 >= 0:
        if (elevation[x][y-1] > num) & (visited_graph[x][y-1] == False):
            dfs(x,y-1,num, elevation, visited_graph)
    if x+1 < len(elevation_graph):
        if (elevation[x+1][y] > num) & (visited_graph[x+1][y] == False):
            dfs(x+1, y, num, elevation_graph, visited_graph)
    if y+1 < len(elevation_graph):
        if (elevation[x][y+1] > num) & (visited_graph[x][y+1] == False):
            dfs(x,y+1,num, elevation, visited_graph)

import sys
n = int(sys.stdin.readline())
visited, elevation, maximum, safeArea = [], [], 0, 0
for i in range(n):
    temp_elevation = list(map(int,sys.stdin.readline().split()))
    elevation.append(temp_elevation)
    maximum = max(maximum,max(temp_elevation))

for i in range(maximum):
    visited = []
    for j in range(n):
        visited.append([False] * n)
    tempNum = 0
    for x in range(n):
        for y in range(n):
            if (elevation[x][y] > i) & (visited[x][y] == False):
                dfs(x,y,i,elevation,visited)
                tempNum += 1
    if safeArea < tempNum:
        safeArea = tempNum
print(safeArea)