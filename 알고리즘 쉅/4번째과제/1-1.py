m,n = map(int,input().split())
graph = []
answer = []
for i in range(m):
    temp = list(map(int,input().split()))
    if i == m-1:
        answer = temp[:]
    graph.append(temp)

for i in range(1,len(answer)):
    answer[i] = answer[i] + answer[i-1]

for i in range(m-2,-1,-1):
    for j in range(n):
        answer[j] = answer[j] + graph[i][j]
    for j in range(1,n):
        answer[j] = min(answer[j], answer[j-1] + graph[i][j])

print(answer[-1])
