def find_square(origin, current, end, size):
    if current > end:
        return 1
    x,y = origin

    if (x+current-1 >= size) or (y+current-1 >= size):
        return 0

    for i in range(current):
        if graph[x+current-1][y+i] == "0" or graph[x+i][y+current-1] == "0":
            return 0
    return find_square(origin, current+1, end)


n = int(input())
available = []
graph = []
answer = []
for i in range(n):
    temp = input()
    graph.append(list(temp))
    for j in range(len(temp)):
        if temp[j] == "1":
            available.append((i,j))

if len(available) > 0:
    answer.append(len(available))

for i in range(2,n+1):
    temp_num = 0
    for j in available:
        temp_num += find_square(j,2,i,n)
    if temp_num == 0:
        break
    answer.append(temp_num)

total = sum(answer)
print(f"total: {total}")
for i in range(len(answer)):
    print(f"size[{i+1}]: {answer[i]}")