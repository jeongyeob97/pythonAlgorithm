from math import ceil, sqrt
from collections import defaultdict
from itertools import combinations
import heapq
def solution(x, y):
    answer = 0
    originList = list(zip(x,y))
    cntDict = {i: [] for i in range(len(x))}
    possible = list(combinations(range(len(x)),2))
    visited = defaultdict(bool)

    for (first, second) in possible:
        origin1 = originList[first]
        origin2 = originList[second]

        distance = calEuclid(origin1, origin2)
        cntDict[first].append((distance,first,second))
        cntDict[second].append((distance, second, first))

    heap = cntDict[0]
    heapq.heapify(heap)

    visited[0] = True

    while heap:
        distance, start, destination = heapq.heappop(heap)
        if not visited[destination]:
            visited[destination] = True
            answer = max(answer,distance)
            for temp in cntDict[destination]:
                heapq.heappush(heap, temp)
    return answer

def calEuclid(origin1, origin2):
    result = sqrt((origin2[0]-origin1[0])**2 + (origin2[1]-origin1[1])**2)
    return ceil(result)

print(solution([1, 2, 6, 8],	[1, 2, 5, 7]))
print(solution([1, 2, 4, 2],	[1, 1, 4, 2]))

print(solution([1,2,1],[1,4,7]))
