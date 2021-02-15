def bfs(start,set1):
    deque_list = deque(graph_dict[start])
    while set1:
        if not deque_list:
            return False
        temp = deque_list.popleft()
        if temp in set1:
            set1.remove(temp)
            for i in graph_dict[temp]:
                deque_list.append(i)
    return True

import sys
from itertools import combinations
from collections import deque

n = int(sys.stdin.readline().strip())
population = list(map(int,sys.stdin.readline().split()))

answer = float('inf')
graph_dict = {}

for i in range(n):
    temp = list(map(int,sys.stdin.readline().split()))
    graph_dict[i+1] = temp[1:]

for i in range(1,n//2+1):
    combination_result = combinations(graph_dict.keys(),i)
    for combi in combination_result:
        side_a = set(combi)
        side_b = set(graph_dict.keys()) - set(combi)
        if bfs(side_a.pop(), side_a) and bfs(side_b.pop(), side_b):
            answer = min(answer,abs(sum([population[i-1] for i in combi]) - sum([population[i-1] for i in set(graph_dict.keys() - set(combi))])))

print([answer,-1][answer == float('inf')])