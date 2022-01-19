from collections import defaultdict, deque



n, m = map(int,input().split())

# 어떤 불을 켰을 때 얘를 움직일 수 있는지에 대한 판단 필요
# 움직일 수 있는 곳인지 확인해야 된다 그렇게 차근 차근 하면 되네
# 상태값 1 방문 가능, -1는 접근 불가
# queue에 어떤 값을 넣을 때 마다 라이트는 별로 필요 없고 그냥 상태값으로 치고 넣자

lights = defaultdict(list)
graph = [[-1] * (n + 2) for i in range(n+2)]

for i in range(m):
    x, y, a, b = map(int, input().split())
    lights[(x,y)].append((a,b))

visited = defaultdict(bool)
queue = deque([(1,1)])
cnt = 1
graph[1][1] = 0
while queue:
    x, y = queue.popleft()
    tx = [1, -1, 0, 0]
    ty = [0, 0, 1, -1]
    if visited[(x, y)]:
        continue
    visited[(x, y)] = True

    for (px, py) in lights[(x,y)]:
        if graph[px][py] == 2 or graph[px][py] == -1:
            cnt += 1

        if graph[px][py] == -1:
            graph[px][py] = 1
        elif graph[px][py] == 2:
            graph[px][py] = 0
            queue.append((px,py))

    for i in range(4):
        dx = x + tx[i]
        dy = y + ty[i]
        if graph[dx][dy] == -1:
            graph[dx][dy] = 2
        elif graph[dx][dy] == 1:
            graph[dx][dy] = 0
            queue.append((dx,dy))



print(cnt)


## 다시 논리 정리
## 시작은 1,1
## 1,1에서 움직일 수 있는 모든 공간에 움직일 수 있다는 마크를 찍는다
## 에서 불을 킬 수 있는 곳에 모두 불을 킨다 그리고 불을 킨 곳에서 queue에 들어갈지 말지에 대한 처리를 한다
## queue에 들어갈지 말지에 대한 모든 정보는 방문한 적이 있는가? 접근 가능한가? 이것인거 같고
## light를 켜줄때 마다 카운트를 쌓아준
