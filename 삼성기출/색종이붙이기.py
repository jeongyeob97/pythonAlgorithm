import sys

paper_cnt = 0
graph = []

for i in range(10):
    temp = []

    for j in list(map(int,sys.stdin.readline().split())):
        if j == 1:
            paper_cnt += 1
        temp.append(j)
    graph.append(temp)

cnt = 0


def dfs(graph, size, origin):
    if size > 5:
        return [1,(size-1)**2]
    x_origin = origin[0]
    y_origin = origin[1]

    for i in range(y_origin, y_origin + size - 1):
        if graph[x_origin + size - 1][i] == 0:
            return [1,(size-1)**2]

    for i in range(x_origin, x_origin + size):
        if graph[i][y_origin + size - 1] == 0:
            return [1,(size-1)**2]

    for i in range(y_origin, y_origin + size - 1):
        graph[x_origin + size - 1][i] = 0

    for i in range(x_origin, x_origin + size):
        graph[i][y_origin + size - 1] = 0

    return dfs(graph, size + 1, origin)

for i in range(10):
    for j in range(10):
        if graph[i][j] == 1:
            temp_cnt, temp_paper =  dfs(graph,2,[i,j])
            cnt += temp_cnt
            paper_cnt -= temp_paper

print(cnt)
print(paper_cnt)

