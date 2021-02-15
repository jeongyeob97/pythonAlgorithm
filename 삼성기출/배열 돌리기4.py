import sys
from itertools import permutations
from copy import deepcopy

n, m, k = map(int,sys.stdin.readline().split())

array = [list(map(int, sys.stdin.readline().split())) for i in range(n)]
standard = deepcopy(array)

answer = float('inf')
spin = [list(map(int, sys.stdin.readline().split())) for i in range(k)]

spin_orders = list(permutations([i for i in range(k)],k))

for i in spin_orders:
    for j in i:
        r, c, s = spin[j]
        start_origin, end_origin = [r-s-1, c-s-1], [r+s-1, c+s-1]
        cnt = (end_origin[0] - start_origin[0] + 1)*(end_origin[1] - start_origin[1] + 1)

        while True:
            if cnt <= 1:
                break
            temp = array[start_origin[0]][start_origin[1]]
            for idx in range(start_origin[1],end_origin[1]):
                array[start_origin[0]][idx+1], temp = temp, array[start_origin[0]][idx+1]

            for idx in range(start_origin[0]+1, end_origin[0]):
                array[idx][end_origin[1]],temp = temp, array[idx][end_origin[1]]

            for idx in range(end_origin[1], start_origin[1]-1,-1):
                array[end_origin[0]][idx], temp = temp,array[end_origin[0]][idx]

            for idx in range(end_origin[0]-1, start_origin[0]-1, -1):
                array[idx][start_origin[1]], temp = temp, array[idx][start_origin[1]]

            cnt -= ((end_origin[0] - start_origin[0] + 1) * 2 + (end_origin[1] - start_origin[1] + 1) * 2) - 4

            start_origin, end_origin = [start_origin[0]+1,start_origin[1]+1], [end_origin[0]-1, end_origin[1]-1]

    answer = min(answer, min([sum(i) for i in array]))

    for j in i:

        r, c, s = spin[j]
        start_origin, end_origin = [r-s-1, c-s-1], [r+s-1, c+s-1]

        for x_idx in range(start_origin[0], end_origin[0]+1):
            for y_idx in range(start_origin[1], end_origin[1]+1):
                array[x_idx][y_idx] = standard[x_idx][y_idx]

print(answer)