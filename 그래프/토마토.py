from collections import deque
import sys
width, depth, height = map(int,sys.stdin.readline().strip().split())
grown, ungrown = deque([]), 0
tomato = []
for i in range(height):
    tomato_temp_list = []
    for j in range(depth):
        line = list(map(int,sys.stdin.readline().strip().split()))
        for k in range(len(line)):
            if line[k] == 1:
                grown.append([[i,j,k],0])
            elif line[k] == 0:
                ungrown += 1
        tomato_temp_list.append(line)
    tomato.append(tomato_temp_list)

def bfs(tomato,ungrown,grown):
    width, depth, height = len(tomato[0][0]), len(tomato[0]), len(tomato)
    answer = 0
    dx, dy, dh = [1,-1,0,0,0,0], [0,0,1,-1,0,0], [0,0,0,0,1,-1]
    while grown:
        t, cnt = grown.popleft()
        answer = cnt
        for i in range(6):
            if (0 <= t[0]+dh[i] < height) and (0 <= t[1]+dy[i] < depth) and (0 <= t[2]+dx[i]<width) and (tomato[t[0]+dh[i]][t[1]+dy[i]][t[2]+dx[i]] == 0):
                tomato[t[0] + dh[i]][t[1] + dy[i]][t[2] + dx[i]] = 1
                grown.append([[t[0]+dh[i], t[1]+dy[i], t[2]+dx[i]], cnt+1])
                ungrown -= 1
    return [-1, answer][ungrown == 0]

if ungrown == 0:
    print(0)
else:
    print(bfs(tomato,ungrown,grown))


























# def bfs(tomato,ungrown,grown):
#     dx = [1,-1,0,0,0,0]
#     dy = [0,0,1,-1,0,0]
#     dh = [0,0,0,0,1,-1]
#     answer = 0
#     tomato_deque = deque(grown)
#     while tomato_deque:
#         t, cnt = tomato_deque.popleft()
#         answer = max(cnt,answer)
#         if visited[t[0]][t[1]][t[2]] == True:
#             continue
#         visited[t[0]][t[1]][t[2]] = True
#         for i in range(6):
#             if i//2 == 0:
#                 if 0 <= t[2] + dx[i] < len(tomato[0][0]):
#                     if (visited[t[0]][t[1]][t[2]+dx[i]] == False) and (tomato[t[0]][t[1]][t[2]+dx[i]] == 0):
#                         tomato[t[0]][t[1]][t[2] + dx[i]] = 1
#                         tomato_deque.append([[t[0],t[1],t[2] + dx[i]],cnt+1])
#                         ungrown -= 1
#                     else:
#                         visited[t[0]][t[1]][t[2] + dx[i]] = True
#             elif i//2 == 1:
#                 if 0 <= t[1] + dy[i] < len(tomato[0]):
#                     if (visited[t[0]][t[1]+dy[i]][t[2]] == False) and (tomato[t[0]][t[1]+dy[i]][t[2]] == 0):
#                         tomato[t[0]][t[1]+dy[i]][t[2]] = 1
#                         tomato_deque.append([[t[0],t[1]+dy[i],t[2]],cnt+1])
#                         ungrown -= 1
#                     else:
#                         visited[t[0]][t[1]+dy[i]][t[2]] = True
#             else:
#                 if 0 <= t[0] + dh[i] < len(tomato):
#                     if (visited[t[0]+dh[i]][t[1]][t[2]] == False) and (tomato[t[0]+dh[i]][t[1]][t[2]] == 0):
#                         tomato[t[0]+dh[i]][t[1]][t[2]] = 1
#                         tomato_deque.append([[t[0]+dh[i],t[1],t[2]],cnt+1])
#                         ungrown -= 1
#                     else:
#                         visited[t[0]][t[1]+dy[i]][t[2]] = True
#     return [-1,answer][ungrown==0]


