def search(graph, adjacent, original,num):
    temp_adjacent = []
    verifyRecur = True
    verifyToggle = True
    for i in range(len(adjacent)):
        if (paper[adjacent[i][0]][adjacent[i][1]] != original) or (len(adjacent) != num):
            verifyRecur = False
            verifyToggle = False
            break
        if i < len(adjacent)//2:
            if adjacent[i][0]+1 >= len(graph):
                verifyRecur = False
                continue
            temp_adjacent.append([adjacent[i][0]+1,adjacent[i][1]])
        elif i == len(adjacent)//2:
            if (adjacent[i][0] + 1 >= len(graph)) or (adjacent[i][1]+1 >= len(graph)):
                verifyRecur = False
                continue

            temp_adjacent.append([adjacent[i][0]+1,adjacent[i][1]])
            temp_adjacent.append([adjacent[i][0]+1,adjacent[i][1]+1])
            temp_adjacent.append([adjacent[i][0],adjacent[i][1]+1])
        else:
            if adjacent[i][1]+1 >= len(graph):
                verifyRecur = False
                continue
            temp_adjacent.append([adjacent[i][0], adjacent[i][1] + 1])
    if verifyToggle:
        for x, y in adjacent:
            graph[x][y] = True
    if verifyRecur:
        search(graph,temp_adjacent,original,num+2)
    return 1
import sys
n = int(sys.stdin.readline())
paper, visited, cnt = [], [], [0,0,0]
for i in range(n):
    visited.append([False]*n)
    paper.append(list(map(int,sys.stdin.readline().split())))
for x in range(n):
    for y in range(n):
        if visited[x][y]:
            continue
        cnt[paper[x][y]+1] += search(visited, [[x,y]], paper[x][y],1)

for i in cnt:
    print(i)