def merge_sort(list1):
    if len(list1) <= 1:
        return list1
    else:
        mid = len(list1) // 2
        temp_list1 = merge_sort(list1[:mid])
        temp_list2 = merge_sort(list1[mid:])

        return merge(temp_list1, temp_list2)


def merge(list1, list2):
    i, j = 0, 0
    temp = []
    while i < len(list1) and j < len(list2):
        print(i,j)
        if list1[i] < list2[j]:
            temp.append(list1[i])
            i += 1
        else:
            temp.append(list2[j])
            j += 1

    while i < len(list1):
        temp.append(list1[i])
        i += 1

    while j < len(list2):
        temp.append(list2[j])
        j += 1
    return temp


n = int(input())
list1 = [int(input()) for i in range(n)]
print(merge_sort(list1))
for i in merge_sort(list1):
    print(i)



