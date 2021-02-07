def search(x, y, d):
    if x < 0:
        return

    if (defense[x][y] == 1) and (y not in pos_dict[x]):
        return [x,y]
    else:
        return bfs([[x,y]], len(defense[0]),y,d)


def bfs(range_list, m, y, d):
    if d == 0:
        return
    temp_list = []
    for i in range_list:
        range_x, range_y = i
        if (defense[range_x][range_y] == 1) and (range_y not in pos_dict[range_x]):
            return[range_x, range_y]

        if range_y <= y:
            if range_y - 1 >= 0:
                temp_list.append([range_x, range_y - 1])
        if range_y == y:
            if range_x - 1 >= 0:
                temp_list.append([range_x - 1, range_y])
        if range_y >= y:
            if range_y + 1 < m:
                temp_list.append([range_x, range_y + 1])

    if len(temp_list) == 0:
        return
    else:
        return bfs(temp_list, m, y, d - 1)

def check(posList, d):
    x = 0
    while len(defense) >= x:
        temp_list = []
        for i in posList:
            origin_x, origin_y = i
            temp_list.append(search(origin_x-x,origin_y,d))
        for i in temp_list:
            if i == None:
                continue
            pos_dict[i[0]].add(i[1])
        x += 1

import sys
from itertools import combinations
n,m,d = map(int,sys.stdin.readline().split())

defense = [list(map(int,sys.stdin.readline().split())) for i in range(n)]

cases = list(combinations([i for i in range(m)], 3))

answer = 0

for i in cases:

    pos_dict = {}

    for j in range(n):
        pos_dict[j] = set()

    pos1, pos2, pos3 = i

    pos_list = [[n-1,pos1], [n-1, pos2], [n-1, pos3]]

    check(pos_list,d)

    total = 0
    for j in range(n):
        total += len(pos_dict[j])

    answer = max(answer,total)

print(answer)

