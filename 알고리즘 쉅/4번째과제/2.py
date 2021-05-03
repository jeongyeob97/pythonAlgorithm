n = int(input())
left = list(map(int,input().split()))
right = list(map(int,input().split()))
leftToRight = list(map(int,input().split()))
rightToLeft = list(map(int,input().split()))

temp_left = 0
temp_right = 0

for i in range(n):
    temp_left += left[i]
    temp_right += right[i]
    temp_left = min(temp_left, temp_right + rightToLeft[i])
    temp_right = min(temp_right, temp_left + leftToRight[i])

print(min(temp_left+ left[-1], temp_right + right[-1]))