def count(graph, start, k):
    isVisited = defaultdict(bool)
    cnt = 0

    queue = deque([(start, float('inf'))])
    isVisited[start] = True
    while queue:
        start, weight = queue.popleft()

        for (node, relevance) in graph[start]:
            if isVisited[node]:
                continue
            isVisited[node] = True
            value = min(relevance, weight)
            if relevance >= k:
                cnt += 1
                queue.append((node, value))

    return cnt

import sys
from collections import defaultdict, deque
input = sys.stdin.readline

n, q = map(int, input().split())
graph = defaultdict(list)

for _ in range(n-1):
    point1, point2, relevance = map(int, input().split())
    graph[point1].append((point2, relevance))
    graph[point2].append((point1, relevance))

for _ in range(q):
    k, start = map(int,input().split())
    print(count(graph, start, k))



