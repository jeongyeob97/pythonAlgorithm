from collections import defaultdict
from itertools import combinations

def solution(orders, course):
    answer = []
    list = getCombinations(orders, course)

    a = defaultdict(int)
    for i in list:
        a[ "".join(sorted("".join(i)))] += 1

    temp_answer = {cnt: [("", 0)] for cnt in course}

    for (key,value) in a.items():
        if temp_answer[len(key)][0][1] < value:
            temp_answer[len(key)] = [(key,value)]
        elif temp_answer[len(key)][0][1] == value:
            temp_answer[len(key)].append((key,value))

    for cnt in course:
        if temp_answer[cnt][0][1] < 2:
            del temp_answer[cnt]

    for i in temp_answer.values():
        for j in i:
            answer.append(j[0])

    return sorted(answer)


def getCombinations(orders, course):
    temp_list = []
    for order in orders:
        for cnt in course:
            temp_list += list(combinations(order, cnt))

    return temp_list







print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]))
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"],[2,3,5]))
print(solution(["XYZ", "XWY", "WXA"], [2,3,4]))
