def solution(places):
    answer = []
    for i in places:
        answer.append(find(i))

    return answer

def find(graph):
    x = [0,0,1,-1]
    y = [1,-1,0,0]
    for i in range(5):
        for j in range(5):
            if graph[i][j] == "P":
                path = deque([(i,j,0)])
                while path:
                    temp = path.popleft()
                    origin_x, origin_y, cnt = temp

                    for i in range(4):
                        temp_x = origin_x + x[i]
                        temp_y = origin_y + y[i]
                        if 0<=temp_x<5 and 0<=temp_y<5 and graph[temp_x][temp_y] != "X" and cnt + 1 < 3:
                            if graph[temp_x][temp_y] == "P":
                                return 0
                            path.append((temp_x,temp_y,cnt+1))
    return 1


from collections import deque
places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
          ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
          ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"],
          ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
          ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]

print(solution(places))