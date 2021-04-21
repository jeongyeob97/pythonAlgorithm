n = int(input())
list1 = [int(input()) for i in range(n)]

for i in range(n-1, 0,-1):
    for j in range(i):
        if list1[j] > list1[j+1]:
            temp = list1[j]
            list1[j] = list1[j+1]
            list1[j+1] = temp

for i in list1:
    print(i)