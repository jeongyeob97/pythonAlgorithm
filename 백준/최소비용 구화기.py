from collections import defaultdict, deque
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = defaultdict(dict)

for i in range(m):
    start, end, cost = map(int,input().split())
    weight = graph[start-1].get(end-1)
    if weight is not None:
       if weight < cost:
            continue
    graph[start-1][end-1] = cost

answer = [float('inf')] * n

start, end = map(int, input().split())

queue = deque([start-1])
answer[start - 1] = 0

while queue:
    city = queue.popleft()
    for (key, value) in graph[city].items():
        if answer[key] > answer[city] + value:
            queue.append(key)
            answer[key] = answer[city] + value

print(answer[end - 1])
