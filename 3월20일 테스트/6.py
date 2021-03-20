n, m = map(int,input().split())

graph = [list(map(int,input().split())) for i in range(m)]
answer = [[0]*n for i in range(m)]

answer[0][0] = graph[0][0]



for i in range(m):
    for j in range(n):
        if i + 1 < m:
            answer[i+1][j] = max(answer[i+1][j], answer[i][j] + graph[i+1][j])
        if j + 1 < n:
            answer[i][j+1] = max(answer[i][j+1], answer[i][j] + graph[i][j+1])


print(answer[-1][-1])