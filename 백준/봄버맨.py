from itertools import combinations

def solution(r,c,n, graph):
    if n == 1:
        return graph

    if (n%2 == 0):
        return [["O"]*c for i in range(r)]

    index_set = set()
    bomb_set = set()
    for i in range(r):
        for j in range(c):
            index_set.add((i,j))
            if graph[i][j] == "O":
                bomb_set.add((i,j))

    final_bomb = cal(n, 1, graph, bomb_set, index_set)

    answer = [["."]*c for i in range(r)]

    for (x,y) in list(final_bomb):
        answer[x][y] = "O"

    return answer

def cal(n, count, graph, bomb, index):
    if count >= n:
        return bomb

    if count % 2 == 0:
        empty_space = explode(bomb, graph)
        bomb_set = index.difference(empty_space)
        return cal(n, count + 1, graph, bomb_set, index)

    return cal(n, count + 1, graph, bomb, index)

def explode(bomb, graph):
    temp_set = set()
    x_list = [1, -1, 0, 0]
    y_list = [0, 0, -1, 1]

    for (x,y) in bomb:
        temp_set.add((x,y))
        for (index_x, index_y) in zip(x_list, y_list):
            if (0<=x+index_x<len(graph)) and (0<=y+index_y<len(graph[0])):
                temp_set.add((x+index_x, y+index_y))

    return temp_set

r, c, n = map(int, input().split())
graph = [list(input())for i in range(r)]
for x in solution(r, c, n, graph):
    print("".join(x))