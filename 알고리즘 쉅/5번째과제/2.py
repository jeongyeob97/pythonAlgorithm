def dfs(grpah, n, m):
    group_cnt = 0
    answer = []
    visited = [False] * n

    for i in range(n):
        if visited[i]:
            continue
        else:
            paths = [i]
            temp_cnt = 0
            while paths:
                value = paths.pop()
                if visited[value] == False:
                    temp_cnt += 1
                    paths.extend(graph[value])
                    visited[value] = True
            answer.append(temp_cnt)
            group_cnt += 1

    return group_cnt, answer


import sys
from collections import deque, defaultdict

input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[] for i in range(n)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

groups, answer_list = dfs(graph, n, m)
print(groups)
print(max(answer_list), min(answer_list))



