n = int(input())
list1 = [int(input()) for i in range(n)]

for i in range(n):
    num = list1[i]
    j = i-1
    while num <= list1[j] and j>=0:
        list1[j+1] = list1[j]
        j-=1
    list1[j+1] = num

print(list1)