n, m = map(int,input().split())
steps = list(map(int, input().split()))
step = list(map(int, input().split()))
answer = [float('inf')]*n

for i in steps:
    answer[i-1] = step[i-1]

for i in range(n):
    for j in steps:
        if i + j < n:
            answer[i+j] = min(answer[i+j], answer[i] + step[i+j])

print([answer[-1], -1][answer[-1] == float('inf')])