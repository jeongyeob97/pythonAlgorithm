import sys
n = int(sys.stdin.readline())
board = [list(map(int,sys.stdin.readline().split())) for i in range(n)]
answer = [[0]*n for i in range(n)]
answer[0][0] = 1
for i in range(n):
    for j in range(n):
        if (i == n-1) and (j == n-1):
            break
        num = board[i][j]
        if i+num < n:
            answer[i+num][j] += answer[i][j]
        if j+num < n:
            answer[i][j+num] += answer[i][j]
print(answer[n-1][n-1])


# def dfs(board, cp, ep):
#     if cp == ep:
#         return
#     elif (cp[0] > ep[0]) or (cp[1] > ep[0]) or (board[cp[0]][cp[1]] == 0):
#         return
#     num = board[cp[0]][cp[1]]
#     # visited[cp[0]][cp[1]] = True
#     return dfs(board,[cp[0]+num, cp[1]], ep) + dfs(board, [cp[0], cp[1]+num], ep)
# print(dfs(board,[0,0], [n-1,n-1]))
# list1 = deque([[0,0]])
# while list1:
#     cp = list1.popleft()
#     if cp == [n-1,n-1]:
#         continue
#     num = board[cp[0]][cp[1]]
#     if (cp[0] + num) <= n-1:
#         visited[cp[0]+num][cp[1]] = visited[cp[0]+num][cp[1]] + visited[cp[0]][cp[1]]
#         list1.append([cp[0]+num,cp[1]])
#     if (cp[1]+ num) <= n-1:
#         visited[cp[0]][cp[1]+num] = visited[cp[0]][cp[1]+num] + visited[cp[0]][cp[1]]
#         list1.append([cp[0], cp[1]+num])
# print(visited[n-1][n-1])






















# def bfs(board,move, ep):
#     sum, temp_list = 0, []
#     for cp in move:
#         if cp == ep:
#             sum += 1
#         elif (cp[0] > ep[0]) or (cp[1] > ep[0]) or (board[cp[0]][cp[1]] == 0):
#             continue
#         num = board[cp[0]][cp[1]]
#         temp_list.append([cp[0] + num, cp[1]])
#         temp_list.append([cp[0], cp[1] + num])
#     return sum + bfs(board,temp_list,ep)

# def bfs(board,move, ep):
#     sum, temp_list = 0, []
#     for cp in move:
#
#         if cp == ep:
#             sum += 1
#         elif (board[cp[0]][cp[1]] == 0) or (visited[cp[0]][cp[1]]):
#             continue
#
#         num = board[cp[0]][cp[1]]
#
#         if cp[0] + num <= ep[0]:
#             temp_list.append([cp[0] + num, cp[1]])
#         if cp[1] + num <= ep[0]:
#             temp_list.append([cp[0], cp[1] + num])
#         visited[cp[0]][cp[1]] = True
#     return sum + bfs(board,temp_list,ep)
# print(bfs(board, [[0,0]], [n-1,n-1]))
