from collections import defaultdict, deque

def solution(maps):
    visited_dict = defaultdict(bool)
    count_dict = defaultdict(bool)
    for x in range(len(maps)):
        for y in range(len(maps[0])):
            point = (x,y)
            if maps[x][y] == "1" and not visited_dict[point]:
                visited_dict, count_dict = search(point, maps, visited_dict, count_dict)

    answer = sorted(count_dict.keys())
    return answer

def search(point, maps, visited_dict, count_dict):
    queue = deque([(point)])
    visited_dict[point] = True
    cnt = 1
    while queue:
        point = queue.popleft()
        possible, visited_dict = findIsland(point, maps, visited_dict)
        cnt += len(possible)
        queue += possible
    count_dict[cnt] = True
    return visited_dict, count_dict

def findIsland(point, maps, visited_dict):
    possible = []
    move = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    x,y = point
    for i in range(4):
        tx = x + move[i][0]
        ty = y + move[i][1]
        if 0 <= tx < len(maps) and 0 <= ty < len(maps[0]) and maps[tx][ty] == "1":
            temp = (tx,ty)
            if not visited_dict[temp]:
                possible.append(temp)
                visited_dict[temp] = True
    return possible, visited_dict




print(solution(["1101110000","1100001000","1000011000","0000000000","0000100100","1110101111"]))
print(solution(["111","001","000","100"]))
print(solution(["1000011","1100001","0000000","1110111"]))
print(solution(["111","101","111"]))