N, K = map(int,input().split())
list1 = []
resume = True
for i in range(N+1):
    list1.append([0]*(N+1))

for k in range(N+1):
    if resume:
        for n in range(N+1):
            if (k == n) or (k == 0):
                list1[k][n] = 1
            elif (k-1 >= 0) and (n-1 >= 0):
                list1[k][n] = list1[k][n-1] + list1[k-1][n-1]
            if (n == N) and (k == K):
                print(list1[k][n]%10007)
                resume = False
                break