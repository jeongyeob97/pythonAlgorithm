import sys
from collections import deque, defaultdict
input = sys.stdin.readline
n = int(input().strip())
m = int(input().strip())
graph = defaultdict(list)
answer = [float('inf')] * (n+1)

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

a,b = map(int, input().split())
answer[a] = 0
path = deque([a])


def bfs(path, b):
    while path:
        value = path.popleft()
        for i in graph[value]:
            if answer[i] > answer[value] + 1:
                answer[i] = answer[value] + 1
                if i == b:
                    return answer[i]
                path.append(i)
    return -1


print(bfs(path,b))
