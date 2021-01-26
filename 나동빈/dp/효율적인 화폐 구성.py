n,m = map(int,input().split())
coin = []
answer = [float('inf')]*(m+1)
for i in range(n):
    coin.append(int(input()))
answer[0] = 0

for i in coin:
    for j in range(i,m+1):
        if answer[j-i] != float('inf'):
            answer[j] = min(answer[j], answer[j-i] + 1)

print([-1,answer[-1]][answer[-1] != 0])