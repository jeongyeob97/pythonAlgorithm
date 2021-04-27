from collections import defaultdict,deque
import sys

input = sys.stdin.readline

city_num = int(input())
bus_num = int(input())

answer = [float('inf')] * city_num
graph = defaultdict(list)

for i in range(bus_num):
    start, end, cost = map(int,input().split())

    graph[start-1].append((end-1, cost))

start_point, end_point = map(int,input().split())
answer[start_point-1] = 0

paths = deque()
paths.append(start_point-1)

while paths:
    start = paths.popleft()
    if start == end_point-1:
        continue
    for end, cost in graph[start]:
        if answer[end] > answer[start]+cost:
            answer[end] = answer[start] + cost
            paths.append(end)

print(answer[end_point-1])



