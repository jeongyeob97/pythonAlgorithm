import sys
import heapq

n,e = map(int,sys.stdin.readline().split())
graph = {}

for i in range(n):
    graph[i + 1] = {}

for i in range(e):
    a,b,c = map(int,sys.stdin.readline().split())
    graph[a][b] = c
    graph[b][a] = c

v1, v2 = map(int,sys.stdin.readline().split())

def dijkstra(start, node_count):
    list1 = [float('inf')] * (node_count+1)

    distance = []
    heapq.heappush(distance, (start,0))
    list1[start] = 0

    while distance:
        node, cnt = heapq.heappop(distance)

        if cnt > list1[node]:
            continue

        for i in graph[node].keys():
            temp = cnt + graph[node][i]
            if list1[i] > temp:
                list1[i] = temp
                heapq.heappush(distance, (i, temp))

    return list1

v1_route, v2_route =  dijkstra(v1, n), dijkstra(v2, n)

first_scenario = v1_route[1] + v1_route[v2] + v2_route[n]
second_scenario = v2_route[1] + v2_route[v1] + v1_route[n]

answer = min(first_scenario, second_scenario)

print([answer, -1][answer == float('inf')])
