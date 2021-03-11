import sys
input = sys.stdin.readline

num = int(input())
stock_array = list(map(int,input().split()))
maximum = float('-inf')
price = [0,0]

for i in range(0,len(stock_array)-1):
    for j in range(i+1,len(stock_array)):
        if (stock_array[i] < stock_array[j]) and (maximum < (stock_array[j] - stock_array[i])):
            maximum = stock_array[j] - stock_array[i]
            price[0], price[1] = stock_array[i], stock_array[j]

if maximum == float('-inf'):
    print(-1)
else:
    print(maximum)
    print(*price)
