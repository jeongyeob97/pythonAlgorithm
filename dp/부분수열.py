n = int(input())
list1 = list(map(int,input().split()))

answer = [1] * n

for i in range(1,n):
    maximum = 0
    for j in range(i):
        if list1[i] > list1[j]:
            maximum = max(answer[j]+1,maximum)
    answer[i] = max(answer[i],maximum)

print(max(answer))