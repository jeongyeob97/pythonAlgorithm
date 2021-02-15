def dfs(origin_x, origin_y):
    global answer

    if graph[origin_x][origin_y] == 1:
        for i in range(5,0,-1):
            if (paper_dict[i] > 0) and (origin_x + i <= 10) and (origin_y + i <= 10):
                check = True
                for j in range(i):
                    for k in range(i):
                        if graph[origin_x+j][origin_y+k] == 0:
                            check = False
                            break
                    if check == False:
                        break

                if check:
                    paper_dict[i] -= 1
                    for j in range(i):
                        for k in range(i):
                            graph[origin_x+j][origin_y+k] = 0

                    if origin_y < 9:
                        dfs(origin_x, origin_y+1)
                    elif origin_x < 9:
                        dfs(origin_x+1, 0)
                    else:
                        temp = 0
                        for x in range(1,6):
                            temp += 5 - paper_dict[x]
                        if answer > temp:
                            answer = temp
                        return

                    paper_dict[i] += 1
                    for j in range(i):
                        for k in range(i):
                            graph[origin_x+j][origin_y+k] = 1

    else:
        if origin_y < 9:
            dfs(origin_x, origin_y + 1)
        elif origin_x < 9:
            dfs(origin_x + 1, 0)
        else:
            temp = 0
            for x in range(1, 6):
                temp += 5 - paper_dict[x]
            if answer > temp:
                answer = temp
            return





import sys
paper_dict = {1: 5, 2: 5, 3: 5, 4:5, 5:5}
graph = [list(map(int,sys.stdin.readline().split())) for i in range(10)]
answer = float('inf')


dfs(0,0)
print([answer, -1][answer == float('inf')])

