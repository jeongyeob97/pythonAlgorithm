from random import randint


# 퀵정렬 함수
def quick_sort(list_array):
    # 재귀 탈출문
    if len(list_array) <= 1:
        return list_array
    # left 피봇보다 작은 수를 넣는 배열, right 피봇보다 큰 수를 넣는 배열
    left, right = [], []
    # 랜덤한 피봇을 위해
    index = randint(0, len(list_array) - 1)
    pivot = list_array[index]

    # 피봇보다 작은 인덱스에 대한 처리
    for a in range(0, index):
        if pivot < list_array[a]:
            right.append(list_array[a])
        else:
            left.append(list_array[a])

    # 피봇보다 큰 수에 대한 처리
    for a in range(index + 1, len(list_array)):
        if pivot < list_array[a]:
            right.append(list_array[a])
        else:
            left.append(list_array[a])

    # 반환문
    return quick_sort(left) + [pivot] + quick_sort(right)


# 이진탐색 함수
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
    # right가 음수일 때 빼고 모두 right을 취하기 때문에 이에 대한 분기문
    if right >= 0:
        return right
    else:
        return left


# 두 수를 찾기 위한 함수
def search(start, end, num):
    index = start
    temp_min, temp_max, total = 0, 0, 0
    while index < end:
        temp_value = list1[index]
        temp_num = s - temp_value
        # temp_num과 작거나 같은 수를 가진 인덱스를 찾기 위해 이분 탐색 사용
        temp_index = binary_search(0, len(list1) - 1, temp_num)
        temp_total = temp_value + list1[temp_index]
        # 현재의 total보다 temp_total 크거나 같고 temp_total이 s보다 작거나 같을 때 분기문 수행
        if (total <= temp_total) and (temp_total <= s):
            # 좁혀오는 형식이기 때문에 문제에서 원하는 값이 같을 때 큰 수가 가장 작은 쌍을 출력할 수 있다.
            total = temp_total
            temp_min, temp_max = temp_value, list1[temp_index]
        index += 1

    return temp_min, temp_max


n = int(input())
list1 = list(map(int, input().split()))
s = int(input())

list1 = quick_sort(list1)
# 원하는 수의 절반에 대한 인덱스를 찾으면 수행했던 작업을 다시 수행할 필요가 없기 때문에 중간값에 대해 이진탐색을 진행한다.
end = binary_search(0, len(list1) - 1, s // 2)

min_num, max_num = search(0, end + 1, s)
print(min_num, max_num)
