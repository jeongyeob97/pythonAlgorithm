from itertools import combinations
from collections import defaultdict
def solution(needs, r):
    cnt_dict = defaultdict(int)
    for possible in combinations(range(len(needs[0])),r):
        cnt_dict[possible] = cal(needs, possible)
    answer = max(cnt_dict.values())
    return answer


def cal(needs, possible):
    cnt = 0

    for i in needs:
        flag = True
        for j in range(len(i)):
            if j not in possible:
                if i[j] == 1:
                    flag = False
                    break
        if flag:
            cnt += 1
    return cnt


print(solution([[ 1, 0, 0 ], [1, 1, 0], [1, 1, 0], [1, 0, 1], [1, 1, 0], [0, 1, 1] ], 2))