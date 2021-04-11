n = int(input())
step = list(map(int,input().split()))
answer = [float('inf')]*n
answer[0], answer[2], answer[3] = step[0], step[2], step[3]

for i in range(n):
    if i + 1 < n:
        answer[i+1] = min(answer[i+1], answer[i] + step[i+1])
    if i + 3 < n:
        answer[i+3] = min(answer[i+3], answer[i] + step[i+3])
    if i + 4 < n:
        answer[i+4] = min(answer[i+4], answer[i] + step[i+4])

print(answer[-1])