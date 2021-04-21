n = int(input())

list1= []
cnt = 0

for i in range(n):
    a,b = map(int,input().split())
    cnt += a
    list1.append([cnt,b])

delay = 0

for i in range(1,n):
    # 밑에 상황일 때 다음 도착 사람이 기다려야 되기 때문
    if list1[i-1][1] > list1[i][0]:
        # 기다린 시간 만큼 딜레이 변수에 넣어준다
        delay += list1[i-1][1] - list1[i][0]
        # list1[i][1]을 실제로 끝나는 시간으로 초기화 해준다
        list1[i][1] = list1[i-1][1] + list1[i][1]
    else:
        # list1[i][1]을 실제로 끝나는 시간으로 초기화 해준다
        list1[i][1] = list1[i][0] + list1[i][1]

# 소수점 이하 1자리까지 출력
print(format(delay/n, ".1f"))