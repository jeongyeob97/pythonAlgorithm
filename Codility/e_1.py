# def solution(schedule):
#     schedule_array = [[False] * 24 for i in range(5)]
#     answer = -1
#     answer = recur(0, schedule_array, schedule)
#     return answer
#
# def recur(index, schedule_array, schedule):
#     if index >= len(schedule_array):
#         return 1
#     count = 0
#
#     for time in schedule[index]:
#         time_index = getIndex(time)
#         if verifyTime(schedule_array, time_index):
#             toggleSchedule(schedule_array, time_index, True)
#             count += recur(index + 1, schedule_array, schedule)
#             toggleSchedule(schedule_array, time_index, False)
#
#     return count
#
# def toggleSchedule(schedule_array, index, isChanging):
#     if len(index) == 1:
#         day_index, time_index = index[0]
#         for i in range(6):
#             schedule_array[day_index][time_index + i] = [False, True][isChanging]
#
#     for (day_index, time_index) in index:
#         for i in range(3):
#             schedule_array[day_index][time_index + i] = [False, True][isChanging]
#
# def getIndex(time):
#     days = {"MO": 0, "TU": 1, "WE": 2, "TH": 3, "FR": 4}
#     splitted = time.split(" ")
#     if len(splitted) > 2:
#         temp = []
#         for i in range(0, len(splitted), 2):
#             day_index = days[splitted[i]]
#             time_split = splitted[i+1].split(":")
#             time_index = int(time_split[0]) - 9 * 2
#             if time_split[1] == "30":
#                 time_index += 1
#             temp.append((day_index, time_index))
#         return temp
#
#     day_index = days[splitted[0]]
#     time_split = splitted[1].split(":")
#     time_index = int(time_split[0]) - 9 * 2
#     if time_split[1] == "30":
#         time_index += 1
#     return [(day_index, time_index)]
#
# def verifyTime(schedule_array, index):
#     count = 0
#     if len(index) == 1:
#         day_index, time_index = index[0]
#         for i in range(6):
#             count += schedule_array[day_index][time_index+i]
#         if count > 0:
#             return False
#         return True
#
#     for (day_index, time_index) in index:
#         for i in range(3):
#             count += schedule_array[day_index][time_index + i]
#         if count > 0:
#             return False
#     return True

# print(solution([["MO 12:00 WE 14:30", "MO 12:00", "MO 15:00", "MO 18:00"], ["TU 09:00", "TU 10:00", "TU 15:00", "TU 18:00"], ["WE 09:00", "WE 12:00", "WE 15:00", "WE 18:00"], ["TH 09:30", "TH 11:30", "TH 15:00", "TH 18:00"], ["FR 15:00", "FR 15:00", "FR 15:00", "FR 15:00"]]))


# -------------

# def solution(stones, k):
#     available = recur(stones, k, {}, "")
#     answer = '-1'
#     if len(available) > 0:
#         answer = sorted(available)[-1]
#
#     return answer

# 이게 리턴되야 하는 경우가 어덜 때 일까? 그냥 리스트로 더해서 주고 시간초과면 유감

# def recur(stones, k, visited, answer):
#     if verify(stones, k):
#         return [answer]
#
#     if visited.get(tuple(stones)):
#         return
#
#     for i in stones:
#         if i < 0:
#             return
#
#     answers = []
#     current_stone = tuple(stones)
#     for idx in range(len(stones)):
#         updateStone(stones,idx, True)
#         returnValue = recur(stones, k, {**visited,  **{current_stone: True}}, answer + f"{idx}")
#         if returnValue:
#             answers += returnValue
#         updateStone(stones, idx, False)
#
#     return answers
#
# def updateStone(stones, idx, isPicked):
#     stones[idx] += [-1,1][isPicked]
#     for i in range(idx):
#         stones[i] += [1,-1][isPicked]
#     for i in range(idx + 1, len(stones)):
#         stones[i] += [1,-1][isPicked]
#
# def verify(stones, k):
#     count = 0
#     for i in stones:
#         if i == k:
#             count += 1
#         elif i == 0:
#             count += 0
#         else:
#             return False
#     if count == 1:
#         return True
#     return False

def solution(stones, k):
    solutions = [[0] * len(stones) for i in range(len(stones))]
    for i in range(len(stones)):
        solutions[i][i] = k
    available = []

    for x in solutions:
        temp = recur(stones, x, "", {})
        if temp:
            available += temp
    for i in map(str, available):
        print(i)

def recur(original, current, answer, visited):
    status_code = verifyStatus(original, current)
    if status_code == 0:
        return
    elif status_code == 1:
        return [answer[::-1]]

    if visited.get(tuple(current)):
        return

    answers = []
    current_stone = tuple(current)
    for idx in range(len(current)):
        updateStone(current,idx, True)
        returnValue = recur(original, current, answer + f"{idx}", {**visited,  **{current_stone: True}})
        if returnValue:
            answers += returnValue
        updateStone(current, idx, False)

def updateStone(stones, idx, isPicked):
    stones[idx] += [1,-1][isPicked]
    for i in range(idx):
        stones[i] += [-1,1][isPicked]
    for i in range(idx + 1, len(stones)):
        stones[i] += [-1,1][isPicked]

def verifyStatus(original, current):
    cnt = 0
    for x,y in zip(original, current):
        if x < 0:
            return 0 # 실행불가
        if x == y:
            cnt += 1
    if cnt == len(original):
        return 1
    return 2


print(solution([1, 3, 2], 3))
print(solution([4, 2, 2, 1, 4], 1))
print(solution([5, 7, 2, 4, 9], 20))