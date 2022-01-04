from collections import defaultdict, deque
def solution(n, path):
    graph = defaultdict(list)
    for (start, end) in path:
        graph[end].append(start)

    for i in range(1, n+1):
        if checkAvailable(graph, i, n):
            return i

    return -1

def checkAvailable(graph, start, n):
    queue = deque([start])
    visited = defaultdict(bool)

    while queue:
        station = queue.popleft()
        if visited[station]:
            continue
        visited[station] = False
        queue += graph[station]

    if len(visited) == n:
        return True

    return False





n = int(input())
path = [map(int, input().split()) for i in range(n-1)]
print(solution(n,path))