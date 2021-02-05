import sys
n = int(sys.stdin.readline().strip())
graph = [list(map(int,sys.stdin.readline().split())) for i in range(n)]
graph[0][1] = [[0,0]]
for i in range(n):
    for j in range(n):
        if (i == n-1) and (j == n-1):
            break
        if (graph[i][j] == 0) or (graph[i][j] == 1):
            continue
        for x,y in graph[i][j]:

            if (i-x == 1) and (j-y == 1):
                if i+1 < n:
                    if graph[i+1][j] != 1:
                        if graph[i + 1][j] == 0:
                            graph[i+1][j] = [[i, j]]
                        else:
                            graph[i+1][j].append([i, j])

                if j + 1 < n:
                    if graph[i][j+1] != 1:
                        if graph[i][j + 1] == 0:
                            graph[i][j + 1] = [[i, j]]
                        else:
                            graph[i][j+1].append([i, j])

                if (i + 1 < n) and (j + 1 < n):
                    if (graph[i][j+1] != 1) and (graph[i+1][j] != 1) and (graph[i+1][j+1] != 1):
                        if graph[i + 1][j + 1] == 0:
                            graph[i + 1][j + 1] = [[i, j]]
                        else:
                            graph[i + 1][j + 1].append([i, j])

            elif j-y == 1:
                if j + 1 < n:
                    if graph[i][j + 1] != 1:
                        if graph[i][j + 1] == 0:
                            graph[i][j + 1] = [[i, j]]
                        else:
                            graph[i][j + 1].append([i, j])

                if (i + 1 < n) and (j + 1 < n):
                    if (graph[i][j + 1] != 1) and (graph[i + 1][j] != 1) and (graph[i + 1][j + 1] != 1):
                        if graph[i + 1][j + 1] == 0:
                            graph[i + 1][j + 1] = [[i, j]]
                        else:
                            graph[i + 1][j + 1].append([i, j])

            elif i-x == 1:
                if i+1 < n:
                    if graph[i+1][j] != 1:
                        if graph[i + 1][j] == 0:
                            graph[i+1][j] = [[i, j]]
                        else:
                            graph[i+1][j].append([i, j])
                if (i + 1 < n) and (j + 1 < n):
                    if (graph[i][j + 1] != 1) and (graph[i + 1][j] != 1) and (graph[i + 1][j + 1] != 1):
                        if graph[i + 1][j + 1] == 0:
                            graph[i + 1][j + 1] = [[i, j]]
                        else:
                            graph[i + 1][j + 1].append([i, j])

if graph[-1][-1] == 0:
    print(0)
else:
    print(len(graph[-1][-1]))