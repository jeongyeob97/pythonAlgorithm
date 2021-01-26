import sys
num, schedule, salary = int(sys.stdin.readline()), [], []

for i in range(num):
    time, pay = list(map(int,sys.stdin.readline().split()))
    schedule.append((time,pay))
    salary.append(pay)

for i in range(num):
    time, pay = schedule[i][0], schedule[i][1]
    if i + time > num:
        salary[i] = 0
        continue
    for j in range(i+time,num):
        if salary[j] <= schedule[j][1] + salary[i]:
            salary[j] = schedule[j][1] + salary[i]

print(max(salary))


# n = int(input())
# T, P = [0 for i in range(n + 1)], [0 for i in range(n + 1)]
# for i in range(n):
#     a, b = map(int, input().split())
#     T[i] = a
#     P[i] = b
#
# # dp[i]는 i번째날까지 일을 했을 때, 최대값이다.
# dp = [0 for i in range(n + 1)]
#
# for i in range(len(T) - 2, -1, -1):  # 역순으로 진행
#     if T[i] + i <= n:  # 날짜를 초과하지 않을 경우.
#         dp[i] = max(P[i] + dp[i + T[i]], dp[i + 1])
#     else:  # 날짜를 초과할 경우.
#         dp[i] = dp[i + 1]
# print(dp[0])