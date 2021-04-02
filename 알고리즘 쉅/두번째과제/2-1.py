import sys
input = sys.stdin.readline
n = int(input())
list1 = list(map(int,input().split()))
k = int(input())

start, end = 0, n-1

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
    return left, right

left, right = binary_search(start,end,k)

if left >= len(list1):
    print(list1[right])
elif right >= 0:
    if abs(k-list1[right]) <= abs(k-list1[left]):
        print(list1[right])
    else:
        print(list1[left])
else:
    print(list1[left])