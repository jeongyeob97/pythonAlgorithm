# import sys
# from itertools import permutations
#
# n = int(sys.stdin.readline().strip())
# innings = [list(map(int,sys.stdin.readline().split())) for i in range(n)]
# temp_list = permutations([i for i in range(1,9)],8)
# maximum = 0
#
# for i in temp_list:
#     line_up = i[:3]+tuple([0])+i[3:]
#     order, cnt = 0, 0
#     for j in range(n):
#         out = 0
#         bases = [0, 0, 0]
#         while out < 3:
#             num = innings[j][line_up[order]]
#             if num == 0:
#                 out += 1
#             else:
#                 for x in range(len(bases)):
#                     if (x+num >= len(bases)) and (bases[x] > 0):
#                         cnt += 1
#                         bases[x] -= 1
#
#                     else:
#                         if bases[x] > 0:
#                             bases[x] -= 1
#                             bases[x+num] += 1
#                 if num > 3:
#                     cnt +=1
#                 else:
#                     bases[num-1] += 1
#             order = (order+1)%9
#     if maximum < cnt:
#         print(line_up)
#         print(cnt)
#         maximum = cnt
# print(maximum)

import sys
from itertools import permutations

n = int(sys.stdin.readline())
answer = 0

innings = [list(map(int,sys.stdin.readline().split())) for i in range(n)]

cases = list(permutations([i for i in range(1,9)],8))

for i in cases:
    order = i[:3] + tuple([0]) + i[3:]
    cnt, index = 0, 0
    for j in range(n):
        out = 0
        first, second, third = 0, 0, 0
        while out < 3:
            num = innings[j][order[index]]
            if num == 0:
                out += 1
            elif num == 1:
                cnt += third
                first, second, third = 1, first, second
            elif num == 2:
                cnt += third + second
                first, second, third = 0, 1, first
            elif num == 3:
                cnt += third + second + first
                first, second, third = 0, 0, 1
            else:
                cnt += third + second + first + 1
                first, second, third = 0, 0, 0

            index = (index + 1) % 9

    answer = max(answer, cnt)

print(answer)