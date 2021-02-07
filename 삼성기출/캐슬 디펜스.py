# def bfs(origin, distance, N, M, idx):
#     x, y = origin
#     if x < 0:
#         return
#     if (area[x][y] == 1) and ((x,y) not in dict_list[idx][x]):
#         dict_list[idx][x].add((x, y))
#         return bfs([x - 1, y], distance, N, M, idx)
#     else:
#         search([[x, y]], distance, y, M, idx)
#         return bfs([x - 1, y], distance, N, M, idx)
#
#
# def search(possibleList, distance, start, M, idx):
#     if distance == 0:
#         return
#     temp_possible_list = []
#     for i in range(len(possibleList)):
#         x, y = possibleList[i]
#         if (area[x][y] == 1) and ((x,y) not in dict_list[idx][x]):
#             dict_list[idx][x].add((x, y))
#             return
#         if y <= start:
#             if (y - 1 >= 0):
#                 temp_possible_list.append([x, y - 1])
#         if y == start:
#             if (x - 1 >= 0):
#                 temp_possible_list.append([x - 1, y])
#         if y >= start:
#             if (y + 1 < M):
#                 temp_possible_list.append([x, y + 1])
#     if len(temp_possible_list) == 0:
#         return
#     else:
#         return search(temp_possible_list, distance - 1, start, M, idx)
#
# import sys
# n,m,d = map(int,sys.stdin.readline().split())
# area = []
# enemy_dict = {}
# answer = 0
# for i in range(n):
#     enemy_dict[i] = 0
#     temp_list = []
#     for j in sys.stdin.readline().split():
#         num = int(j)
#         if num == 1:
#             enemy_dict[i] += 1
#         temp_list.append(num)
#     area.append(temp_list)
#
# from itertools import combinations
#
# cases = list(combinations([i for i in range(m)],3))
#
# for i in cases:
#     dict_list = [{},{},{}]
#
#     for j in range(n):
#         dict_list[0][j] = set()
#         dict_list[1][j] = set()
#         dict_list[2][j] = set()
#
#     num1, num2, num3 = i
#
#     case_list = [[n-1,num1],[n-1,num2],[n-1,num3]]
#
#     for j in range(len(case_list)):
#         bfs(case_list[j],d,n,m,j)
#
#     temp_answer = 0
#
#     for j in range(n):
#         temp_answer += len(dict_list[0][j] | dict_list[1][j] | dict_list[2][j])
#
#     # answer = max(answer, temp_answer)
#     if answer < temp_answer:
#         answer = temp_answer
#         print(case_list)
#
#
# print(answer)

# def search(x, y, d, idx):
#     if x < 0:
#         return
#
#     if (defense[x][y] == 1) and (y not in pos_dict[idx][x]):
#         pos_dict[idx][x].add(y)
#     else:
#         bfs([[x,y]], len(defense[0]),y,d,idx)
#
#     search(x - 1, y, d, idx)
#
#
# def bfs(range_list, m, y, d, idx):
#     if d == 0:
#         return
#     temp_list = []
#     for i in range_list:
#         range_x, range_y = i
#         if (defense[range_x][range_y] == 1) and (range_y not in pos_dict[idx][range_x]):
#             pos_dict[idx][range_x].add(range_y)
#             return
#
#         if range_y <= y:
#             if range_y - 1 >= 0:
#                 temp_list.append([range_x, range_y - 1])
#         if range_y == y:
#             if range_x - 1 >= 0:
#                 temp_list.append([range_x - 1, range_y])
#         if range_y >= y:
#             if range_y + 1 < m:
#                 temp_list.append([range_x, range_y + 1])
#
#     if len(temp_list) == 0:
#         return
#     else:
#         bfs(temp_list, m, y, d - 1, idx)
#
# import sys
# from itertools import combinations
# n,m,d = map(int,sys.stdin.readline().split())
#
# defense = [list(map(int,sys.stdin.readline().split())) for i in range(n)]
#
# cases = list(combinations([i for i in range(m)], 3))
#
# answer = 0
#
# for i in cases:
#
#
#     pos_dict = [{},{},{}]
#
#     for j in range(n):
#         pos_dict[0][j] = set()
#         pos_dict[1][j] = set()
#         pos_dict[2][j] = set()
#
#     pos1, pos2, pos3 = i
#
#     pos_list = [[n-1,pos1], [n-1, pos2], [n-1, pos3]]
#
#     for j in range(len(pos_list)):
#         origin_x, origin_y = pos_list[j]
#         search(origin_x, origin_y, d, j)
#
#     total = 0
#     print("!@#!!@!@")
#     for j in range(n):
#         print(len(pos_dict[0][j] | pos_dict[1][j] | pos_dict[2][j]))
#         total += len(pos_dict[0][j] | pos_dict[1][j] | pos_dict[2][j])
#     print("!@#!@#!@#")
#     answer = max(answer,total)
#
# print(answer)

