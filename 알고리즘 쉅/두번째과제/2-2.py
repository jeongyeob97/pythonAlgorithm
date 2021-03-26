from random import randint

def quick_sort(list_array):
    if len(list_array) <= 1:
        return list_array

    left, right = [], []
    index = randint(0,len(list_array)-1)
    pivot = list_array[index]

    for a in range(0, index):
        if pivot < list_array[a]:
            right.append(list_array[a])
        else:
            left.append(list_array[a])


    for a in range(index+1, len(list_array)):
        if pivot < list_array[a]:
            right.append(list_array[a])
        else:
            left.append(list_array[a])

    return quick_sort(left) + [pivot] + quick_sort(right)

def recur (start, end, num):
    if start == end:
        return start
    index = (end + start) // 2
    if list1[index] > num:
        return recur(start, index-1, num)
    else:
        return recur(index+1, end, num)

n = int(input())
list1 = list(map(int,input().split()))
s = int(input())

list1 = quick_sort(list1)

index = recur(0,len(list1),s)

minNum, maxNum = 0, 0

for i in range(index,0,-1):
    if minNum + maxNum > list1[i] + list1[i-1]:
        break
    for j in range(i):
        if list1[i] + list1[j] > s:
            continue
        if minNum + maxNum < list1[i] + list1[j]:
            minNum, maxNum = list1[j], list1[i]
        elif minNum + maxNum == list1[i] + list1[j]:
            if maxNum > list1[j]:
                minNum, maxNum = list1[j], list1[i]

print(minNum, maxNum)

