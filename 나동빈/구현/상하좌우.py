n = int(input())
dict1 = {"R":[0,1], "L":[0,-1], "U":[-1,0], "D":[1,0]}
list1 = input().split()
start = [0,0]
for i in list1:
    direction = dict1[i]
    if (0 <= start[0] + direction[0] < n) and (0 <= start[1] + direction[1] < n):
        start = [start[0] + direction[0], start[1] + direction[1]]

print(start[0]+1, start[1] + 1)