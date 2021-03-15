n = int(input())
list1 = list(map(int,input().split()))
answer = [0] * len(list1)

for i in range(1,len(list1)):
    for j in range(i-1,-1,-1):
        if list1[i] > list1[j]:
            answer[j] = max(answer[j], list1[i]-list1[j])
        else:
            break

print(sum(answer))