n = int(input())

list1 = list(map(int, input().split()))
temp = [[0,0] for i in range(len(list1))]
for i in range(1, len(list1)):
    if list1[i - 1] < list1[i]:
        temp[i] = [list1[i], list1[i - 1]]
        list1[i] = list1[i - 1]

answer_list = sorted(temp, key=lambda x: x[0], reverse = True)
answer_list = sorted(answer_list, key=lambda x: x[0] - x[1])

if answer_list[-1][0] - answer_list[-1][1] == 0:
    print(-1)
else:
    answer = answer_list.pop()
    print(answer[0] - answer[1])
    print(answer[1], answer[0])