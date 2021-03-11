import sys
input = sys.stdin.readline
n = int(input())
stock_array = list(map(int,input().split()))
cnt_array = [0] * n
maximum = 0

for i in range(1,len(stock_array)):
    if stock_array[i-1] < stock_array[i]:
        cnt_array[i] = cnt_array[i-1] + 1
        maximum = max(maximum, cnt_array[i])

print(maximum)