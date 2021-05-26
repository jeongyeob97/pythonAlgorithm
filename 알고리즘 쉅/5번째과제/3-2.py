import sys
from collections import defaultdict, deque

input = sys.stdin.readline

n = int(input().strip())
lanes = defaultdict(set)
subway = defaultdict(list)

for _ in range(n):
    n, station_a, station_b = input().split()
    n = int(n)
    lanes[station_a].add(n)
    lanes[station_b].add(n)
    subway[station_a].append(station_b)
    subway[station_b].append(station_a)

answer = defaultdict(list)

start, end = input().split()
available = deque([start])

answer[start] = [lanes[start], 0, [start]]

while available:
    station = available.popleft()
    lane, transfer, path = answer[station]
    for next in subway[station]:
        if answer[next] == []:
            if len(lane&lanes[station]) >= 1:
                answer[next] = [lane&lanes[station], transfer, path + [next]]
            else:
                answer[next] = [lanes[next], transfer + 1, path + [next]]
            if next != end:
                available.append(next)


        else:
            answer_lane, answer_transfer, answer_path = answer[next]
            temp = []
            if len(lane&lanes[station]) >= 1:
                temp = [lane, transfer, path + [next]]
            else:
                temp = [lanes[next], transfer + 1, path + [next]]

            if len(answer_path) > len(temp[2]):
                answer[next] = temp
                if next != end:
                    available.append(next)
            elif len(answer_path) == len(temp[2]):
                if answer_transfer > temp[1]:
                    answer[next] = temp
                    if next != end:
                        available.append(next)

if answer[end] == []:
    print(-1)
else:
    print(len(answer[end][2]))
    print(answer[end][2])


