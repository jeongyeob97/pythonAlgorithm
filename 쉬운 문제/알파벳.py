def check(x, y, number, visited):
    if graph[x][y] in visited:
        return number
    visited.append(graph[x][y])
    x_axis = [1, -1, 0, 0]
    y_axis = [0, 0, 1, -1]
    maximum = 0
    for i in range(4):
        temp_x = x + x_axis[i]
        temp_y = y + y_axis[i]
        if (-1<temp_x<len(graph)) and (-1<temp_y<len(graph[0])):
            maximum = max(maximum,check(temp_x,temp_y,number+1,visited[:]))
    return maximum

import sys

hor, ver = map(int,sys.stdin.readline().split())
graph = []

for i in range(hor):
    graph.append(list(sys.stdin.readline().strip()))

print(check(0,0,0,[]))
