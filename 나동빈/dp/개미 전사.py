n = int(input())
list1 = list(map(int,input().split()))
answer = [0]*n
answer[0] = list1[0]
answer[1] = max(list1[1],answer[0])
for i in range(2,n):
    answer[i] = max(answer[i-1], answer[i-2] + list1[i])
print(answer)
print(answer[n-1])

