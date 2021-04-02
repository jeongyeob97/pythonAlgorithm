n = int(input())

list1= []
cnt = 0

for i in range(n):
    a,b = map(int,input().split())
    cnt += a
    list1.append([cnt,b])

delay = 0

for i in range(1,n):
    if list1[i-1][1] > list1[i][0]:
        delay += list1[i-1][1] - list1[i][0]
        list1[i][1] = list1[i-1][1] + list1[i][1]
    else:
        list1[i][1] = list1[i][0] + list1[i][1]

print(format(delay/n, ".1f"))