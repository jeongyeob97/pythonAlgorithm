n = int(input())
list1 = [int(input()) for i in range(n)]


def quicksort(temp_list1):
    if len(temp_list1) <= 1:
        return temp_list1
    pivot = temp_list1[0]
    left, right = [], []
    for i in range(1, len(temp_list1)):
        if pivot > temp_list1[i]:
            left.append(temp_list1[i])
        else:
            right.append(temp_list1[i])

    return quicksort(left) + [pivot] + quicksort(right)

for i in quicksort(list1):
    print(i)

