import sys
from itertools import combinations

input = sys.stdin.readline

house, chicken = map(int, input().split())

house_list, chicken_list = [], []

for i in range(house):
    temp_list = list(map(int, input().split()))
    for j in range(len(temp_list)):
        if temp_list[j] == 1:
            house_list.append((i,j))
        elif temp_list[j] == 2:
            chicken_list.append((i,j))

cases = combinations(chicken_list,chicken)

cnt = float('inf')
for i in cases:
    temp_cnt = 0
    for house_x, house_y in house_list:
        minimum = float('inf')
        for chicken_x, chicken_y in i:
            minimum = min(abs(chicken_x-house_x) + abs(chicken_y-house_y), minimum)
        temp_cnt += minimum
    cnt = min(cnt,temp_cnt)

print(cnt)




