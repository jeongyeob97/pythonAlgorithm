import heapq
from sys import stdin
heapList = []
for i in range(int(stdin.readline())):
    input_num = int(stdin.readline())
    if input_num == 0:
        if len(heapList) == 0:
            print(0)
        else:
            print(-heapq.heappop(heapList))
    else:
        heapq.heappush(heapList, -input_num)