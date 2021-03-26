n = int(input())
list1 = list(map(int,input().split()))
k = int(input())
start, end = 0, n-1

def recur (start, end, num):
    if start == end:
        return start
    index = (end + start) // 2
    if list1[index] > num:
        return recur(start, index-1, num)
    else:
        return recur(index+1, end, num)

print(list1[recur(start, end, k)])