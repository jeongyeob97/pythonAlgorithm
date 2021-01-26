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
