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

def binary_search(start, end, num):
    left = start
    right = end
    while left <= right:
        mid = (left + right) // 2
        temp_num = list1[mid]

        if (temp_num > num):
            right = mid - 1
        else:
            left = mid + 1
    if right >= 0:
        return right
    else:
        return left

def search(start, end, num):
    index = start
    temp_min, temp_max, total = 0, 0, 0
    while index < end:
        temp_value = list1[index]
        temp_num = s- temp_value
        temp_index = binary_search(0, len(list1)-1, temp_num)
        temp_total = temp_value + list1[temp_index]
        if (total <= temp_total) and (temp_total <= s):
            total = temp_total
            temp_min, temp_max = temp_value, list1[temp_index]
        index += 1



    return temp_min, temp_max

n = int(input())
list1 = list(map(int,input().split()))
s = int(input())

list1 = quick_sort(list1)
end = binary_search(0,len(list1)-1, s//2)

min_num, max_num = search(0,end+1, s)
print(min_num, max_num)






































#
# from random import randint
#
# def quick_sort(list_array):
#     if len(list_array) <= 1:
#         return list_array
#
#     left, right = [], []
#     index = randint(0,len(list_array)-1)
#     pivot = list_array[index]
#
#     for a in range(0, index):
#         if pivot < list_array[a]:
#             right.append(list_array[a])
#         else:
#             left.append(list_array[a])
#
#
#     for a in range(index+1, len(list_array)):
#         if pivot < list_array[a]:
#             right.append(list_array[a])
#         else:
#             left.append(list_array[a])
#
#     return quick_sort(left) + [pivot] + quick_sort(right)
#
# def binary_search(start, end, num):
#     left = start
#     right = end
#     while left <= right:
#         mid = (left + right) // 2
#         temp_num = list1[mid]
#
#         if (temp_num > num):
#             right = mid - 1
#         else:
#             left = mid + 1
#     return left, right
#
# n = int(input())
# list1 = list(map(int,input().split()))
# s = int(input())
#
# list1 = quick_sort(list1)
# left,right = binary_search(0,len(list1)-1, s)
#
# index = 0
# if left >= len(list1):
#     index = right
# elif right >= 0:
#     index = right
# else:
#     index = left
#
# maxNum, minNum = 0,0
# total = 0
#
# for i in range(index,0,-1):
#     for j in range(i-1,-1,-1):
#         sum = list1[i] + list1[j]
#         if (sum <= s) and (sum > total):
#             if maxNum + minNum < i+j:
#                 maxNum, minNum = i,j
#                 total = list1[maxNum] + list1[minNum]
#         elif sum == total:
#             if i-j < maxNum - minNum:
#                 maxNum, minNum = i,j
#         elif list1[i] + list1[j] > s:
#             continue
#         else:
#             break
# print(list1[minNum], list1[maxNum])