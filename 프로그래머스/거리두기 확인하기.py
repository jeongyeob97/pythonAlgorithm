from collections import deque

def solution(places):
    answer = []
    for place in places:
        answer.append(int(search(place)))
    return answer


def search(place):
    for line in range(len(place)):
        for column in range(len(place[line])):
            if place[line][column] == "P":
                if not checkDistance(place, line, column):
                    return False

    return True

def checkDistance(place, line, column):
    available = deque([(line, column, 0)])
    x_list = [0, 0, 1, -1]
    y_list = [1, -1, 0, 0]qqqq

    while available:
        temp_line, temp_column, temp_count = available.popleft()
        if temp_count >= 2:
            continue
        for x,y in zip(x_list,y_list):
            if not isInBoundary(temp_line + x) & isInBoundary(temp_column + y):
                continue
            if temp_line + x == line and temp_column + y == column:
                continue

            if place[temp_line + x][temp_column + y] == "P":
                return False
            elif place[temp_line + x][temp_column + y] == "X":
                continue

            xxx = temp_line + x
            yyy = temp_column + y



            available.append((temp_line + x, temp_column + y, temp_count + 1))

    return True




def isInBoundary(num):
    return 0 <= num <= 4



































print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))

print(solution([["PXPOO", "XPOOP","XXXXX","POXPX","OOPXP"]]))
