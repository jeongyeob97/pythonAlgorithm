import sys

n,m = map(int,sys.stdin.readline().split())

graph = [[]for _ in range(n+1)]

for _ in range(m):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))

def bellman(n):
    answer = [float('inf')] * (n+1)
    answer[1] = 0

    for _ in range(1,n):
        for i in range(1,n+1):
            if answer[i] == float('inf'):
                continue
            for node, weight in graph[i]:
                if answer[node] > answer[i] + weight:
                    answer[node] = answer[i] + weight


    for i in range(1,n+1):
        if answer[i] == float('inf'):
            continue
        for node, weight in graph[i]:
            if answer[node] > answer[i] + weight:
                print(-1)
                sys.exit()

    for i in range(2,n+1):
        print(answer[i] if answer[i] != float('inf') else -1)

bellman(n)