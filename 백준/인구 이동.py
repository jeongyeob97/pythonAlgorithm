import sys
from collections import deque

def solution (n, small, big):
    coordinates = [(i,j) for i in range(n) for j in range(i%2,n,2)]
    all_coordinate = [(i,j) for i in range(n) for j in range(n)]
    lands = [list(map(int,input().split())) for i in range(n)]
    count = 0

    while True:
        if not search(all_coordinate, coordinates, lands, small, big):
            return count
        count += 1

def search(all_coordinate, coordinates, lands, small, big):
    is_moved = False
    isVisited = {i: False for i in all_coordinate}
    tx, ty = [0,0,-1,1], [1,-1,0,0]

    for coordinate in coordinates:
        if isVisited[coordinate]:
            continue
        temp = [coordinate]
        queue = deque([coordinate])
        count = 0
        isVisited[(coordinate[0],coordinate[1])] = True

        while queue:
            x, y = queue.popleft()
            count += lands[x][y]
            for i in range(4):
                rx = tx[i] + x
                ry = ty[i] + y

                if 0 <= rx < len(lands) and 0 <= ry <len(lands):
                    if isVisited[(rx, ry)]:
                        continue

                    if small <= abs(lands[x][y] - lands[rx][ry]) <= big:
                        queue.append((rx,ry))
                        temp.append((rx,ry))
                        isVisited[(rx, ry)] = True

        count = count // len(temp)

        if len(temp) > 1:
            is_moved = True
            for x,y in temp:
                lands[x][y] = count

    return is_moved

input = sys.stdin.readline

n, small, big = map(int, input().split())
print(solution(n, small, big))