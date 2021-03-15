# import sys
# input = sys.stdin.readline
#
# num = int(input())
# stock_array = list(map(int,input().split()))
# maximum = float('-inf')
# price = [0,0]
#
# for i in range(0,len(stock_array)-1):
#     for j in range(i+1,len(stock_array)):
#         if (stock_array[i] < stock_array[j]) and (maximum < (stock_array[j] - stock_array[i])):
#             maximum = stock_array[j] - stock_array[i]
#             price[0], price[1] = stock_array[i], stock_array[j]
#
# if maximum == float('-inf'):
#     print(-1)
# else:
#     print(maximum)
#     print(*price)


# 우리 한번 디피로 풀어보아요

n = int(input())

list1 = list(map(int, input().split()))
temp = [[0,0] for i in range(len(list1))]
for i in range(1, len(list1)):
    if list1[i - 1] < list1[i]:
        temp[i] = [list1[i], list1[i - 1]]
        list1[i] = list1[i - 1]

answer_list = sorted(temp, key=lambda x: x[0] - x[1])

if answer_list[-1][0] - answer_list[-1][1] == 0:
    print(-1)
else:
    answer = answer_list.pop()
    print(answer[0] - answer[1])
    print(answer[1], answer[0])

