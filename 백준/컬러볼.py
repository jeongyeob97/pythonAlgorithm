from collections import defaultdict
import sys

input = sys.stdin.readline

n = int(input())
balls = []
for i in range(n):
    color, size = map(int, input().split())
    balls.append((size, color, i))

balls.sort(key = lambda x: (x[0], x[1]))

color_count = defaultdict(int)
total_count = 0
balls_count = defaultdict(int)

## 커졌을 때 업데이트 하는 방법
temp = 0
for size, color, idx in balls:
    second = balls[temp]

    while balls[temp][0] < size:
        total_count += balls[temp][0]
        color_count[balls[temp][1]] += balls[temp][0]
        temp += 1
        second = balls[temp]

    balls_count[idx] = total_count - color_count[color]

for i in range(n):
    print(balls_count[i])
