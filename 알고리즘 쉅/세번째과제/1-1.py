n = int(input())
list1 = [0]*(n+1)
list1[0] = 1

for i in range(n+1):
    if i + 1 <= n:
        list1[i+1] += list1[i]
    if i + 3 <= n:
        list1[i+3] += list1[i]
    if i + 4 <= n:
        list1[i+4] += list1[i]

print(list1[-1])