from itertools import combinations
from collections import defaultdict
import heapq
import sys

def cal(first, second):
    fx, fy = first[0]
    sx, sy = second[0]
    return (fx-sx)**2 + (fy-sy)**2

def findParent(parent, idx):
    if parent[idx] != idx:
        parent[idx] = findParent(parent, parent[idx])
    return parent[idx]

def unionParent(parent, a, b):
    a = findParent(parent, a)
    b = findParent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] =b


def solution(n,c):
    fields = []
    heap = []

    for i in range(n):
        x, y = map(int, input().split())
        fields.append(((x, y), i))

    for first, second in combinations(fields, 2):
        num = cal(first,second)
        if num < c:
            continue
        heapq.heappush(heap, (num, first[1], second[1]))

    # isVisited = defaultdict(bool)
    nodes = set()
    cnt = 0

    if len(heap) < n-1:
        return -1

    parents = [0] + [i+1 for i in range(n)]

    while heap:
        weight, first, second = heapq.heappop(heap)
        if findParent(parents, first) == findParent(parents, second):
            continue
        cnt += weight
        nodes.update([first, second])
        # isVisited[first] = True
        # isVisited[second] = True
        unionParent(parents, first, second)

        if len(nodes) == n:
            return cnt
    return -1

input = sys.stdin.readline

n, c = map(int, input().split())
print(solution(n,c))
