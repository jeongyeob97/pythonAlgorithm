# def solution(land):
#     answer = start(land)
#
#     return answer
#
# def start(land):
#     current_line = land[0][:]
#     next_line = [0]*4
#     for i in range(len(land)-1):
#         for index in range(4):
#             maximum = []
#             for j in range(index):
#                 maximum.append(land[i][j] + land[i+1][index])
#             for j in range(index+1, 4):
#                 maximum.append(land[i][j] + land[i+1][index])
#
#             land[i+1][index] = max(maximum)
#
#     return max(land[-1])
#
# print(solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]]	))

from math import ceil

def solution(progresses, speeds):
    answer = []
    index = 0
    while index < len(progresses):
        cnt = cal(progresses, speeds, index)
        answer.append(cnt)
        index += cnt
    return answer

def cal(progresses, speeds, index):
    rest = 100-progresses[index]
    days = ceil(rest/speeds[index])

    for i in range(index,len(progresses)):
        progresses[i] += (speeds[i] * days)

    cnt = 0
    for i in range(index,len(progresses)):
        if progresses[i] < 100:
            break
        cnt += 1
    return cnt
print(solution([93, 30, 55], [1, 30, 5]	))
print(solution([95, 90, 99, 99, 80, 99]	, [1, 1, 1, 1, 1, 1]	))