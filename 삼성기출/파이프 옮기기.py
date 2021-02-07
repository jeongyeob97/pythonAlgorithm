# import sys
# n = int(sys.stdin.readline().strip())
# graph = []
# for i in range(n):
#     temp_graph = []
#     for j in sys.stdin.readline().split():
#         temp_graph.append([int(j)])
#     graph.append(temp_graph)
#
# graph[0][1] = [2]
#
# # 2일때 가로
# # 3일때 대각
# # 4일때 세로
# # 범위 안에 들어가있을 때 가능
#
# def check_graph(type, origin, num):
#     x,y = origin
#     if (y+1 < n) and (x+1 < n) and (graph[x][y+1] != [1]) and (graph[x+1][y] != [1]) and (graph[x+1][y+1] != [1]):
#         if graph[x+1][y+1] == [0]:
#             graph[x+1][y+1] = [3]
#         else:
#             graph[x+1][y+1].append(3)
#
#     if (type == 2) or (type == 3):
#         if (y+1 < n) and (graph[x][y+1] != [1]):
#             if graph[x][y+1] == [0]:
#                 graph[x][y+1] = [2]
#             else:
#                 graph[x][y+1].append(2)
#
#     if (type == 4) or (type == 3):
#         if (x+1 < n) and (graph[x+1][y] != [1]):
#             if graph[x+1][y] == [0]:
#                 graph[x+1][y] = [4]
#             else:
#                 graph[x+1][y].append(4)
#
# for i in range(n):
#     for j in range(n):
#         if (i == n-1) and (j == n-1):
#             break
#         if (graph[i][j] == [0]) or (graph[i][j] == [1]):
#             continue
#         for x in graph[i][j]:
#             check_graph(x, [i,j], n)
#
# if graph[n-1][n-1] == [0]:
#     print(0)
# else:
#     print(len(graph[n-1][n-1]))


# 2는 가로
# 3은 대각
# 4는 세로

# def add_path(x,y, num):
#     for i in graph[x][y].keys():
#         if (y + 1 < num) and (x + 1 < num) and (graph[x][y + 1] != "1") and (graph[x + 1][y + 1] != "1") and (
#                 graph[x + 1][y] != "1"):
#             if (graph[x + 1][y + 1] == "0") :
#                 graph[x + 1][y+1] = {3:1}
#             elif (3 not in graph[x+1][y+1]):
#                 graph[x+1][y+1][3] = 1
#             else:
#                 if i == 2:
#                     graph[x + 1][y + 1][3] += graph[x][y][2]
#                 elif i == 3:
#                     graph[x + 1][y + 1][3] += graph[x][y][3]
#                 else:
#                     graph[x + 1][y + 1][3] += graph[x][y][4]
#
#
#         if i <= 3:
#             if (y+1 < num) and (graph[x][y+1] != "1"):
#                 if (graph[x][y+1] == "0") :
#                     graph[x][y+1] = {2:1}
#                 elif 2 not in graph[x][y+1]:
#                     graph[x][y+1][2] = 1
#                 else:
#                     if i == 2:
#                         graph[x][y + 1][3] += graph[x][y][2]
#                     else:
#                         graph[x][y + 1][3] += graph[x][y][3]
#
#         if i >= 3:
#             if (x+1 < num) and (graph[x+1][y] != "1"):
#                 if (graph[x+1][y] == "0"):
#                     graph[x+1][y] = {4:1}
#                 elif (4 not in graph[x+1][y]):
#                     graph[x+1][y][4] = 1
#                 else:
#                     if i == 4:
#                         graph[x + 1][y][3] += graph[x][y][4]
#                     else:
#                         graph[x + 1][y][3] += graph[x][y][3]
#
# def start(n):
#     for i in range(n):
#         for j in range(n):
#             if (i == n - 1) and (j == n - 1):
#                 break
#             if (graph[i][j] == "0") or (graph[i][j] == "1"):
#                 continue
#             add_path(i, j, n)
#
#     if graph[-1][-1] == "0":
#          print(0)
#     else:
#         print(graph[-1][-1])
#         print(sum(graph[-1][-1][i] for i in graph[-1][-1].keys()))
#
# import sys
# n = int(sys.stdin.readline().strip())
# graph = [sys.stdin.readline().split() for i in range(n)]
#
# graph[0][1] = {2:1}
#
# if graph[-1][-1] == "1":
#     print(0)
# else:
#     start(n)
#


# 인덱스 0은 가로
# 인덱스 1은 세로
# 인덱스 2는 대각

import sys

n = int(sys.stdin.readline().strip())

graph = []
for i in range(n):
    temp = []
    for j in sys.stdin.readline().split():
        if j == "0":
             temp.append([0,0,0])
        else:
            temp.append(j)
    graph.append(temp)

graph[0][1][0] = 1

for i in range(n):
    for j in range(n):
        if i == 0 and j < 2:
            continue
        if graph[i][j] == "1":
            continue
        if (j-1 >= 0) and (graph[i][j-1] != "1"):
            graph[i][j][0] = graph[i][j-1][0] + graph[i][j-1][2]
        if (i-1 >= 0) and (graph[i-1][j] != "1"):
            graph[i][j][1] = graph[i-1][j][1] + graph[i-1][j][2]
        if (i-1 >= 0) and (j-1 >= 0) and (graph[i-1][j-1] != "1") and (graph[i][j-1] != "1") and (graph[i-1][j] != "1"):
            graph[i][j][2] = sum(graph[i-1][j-1])

if (graph[-1][-1] == "1") or (sum(graph[-1][-1]) == 0):
    print(0)
else:
    print(sum(graph[-1][-1]))