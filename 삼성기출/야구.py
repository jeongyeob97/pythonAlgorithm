import sys
from itertools import permutations

n = int(sys.stdin.readline().strip())
innings = [ list(map(int,sys.stdin.readline().split())) for i in range(n)]
temp_list = permutations([i for i in range(1,9)],8)
maximum = 0

for i in temp_list:
    line_up = i[:3]+tuple([0])+i[3:]
    order, cnt = 0, 0
    for j in range(n):
        out = 0
        bases = [0, 0, 0]
        while out < 3:
            num = innings[j][line_up[order]]
            if num == 0:
                out += 1
            else:
                for i in range(len(bases)):
                    if (i+num >= len(bases)) and (bases[i] > 0):
                        cnt += 1
                        bases[i] -= 1

                    else:
                        if bases[i] > 0:
                            bases[i] -= 1
                            bases[i+num] += 1
                if num > 3:
                    cnt +=1
                else:
                    bases[num-1] += 1
            order = (order+1)%9
    if maximum < cnt:
        print(line_up)
        print(cnt)
        maximum = cnt
print(maximum)