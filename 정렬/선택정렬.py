# 선택 정렬
n = int(input())
list1 = [int(input()) for i in range(n)]

for i in range(n):
    small_num_index = i
    for j in range(i,n):
        if list1[small_num_index] > list1[j]:
            small_num_index = j
    temp = list1[small_num_index]
    list1[small_num_index] = list1[i]
    list1[i] = temp

for i in list1:
    print(i)