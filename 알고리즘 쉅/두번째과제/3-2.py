n = int(input())
list1 = []
cnt, delay = 0, 0
# 심사대가 2개이기 때문에 이에 대한 처리를 해준다
immi1, immi2 = [0, 0], [0, 0]

for i in range(n):
    a,b = map(int,input().split())
    cnt += a
    list1.append([cnt,b])

for i in list1:
    # 효율적인 진행을 위해 가장 빨리는 끝나는 심사대에 i를 넣어준다
    if immi1[1] > immi2[1]:
        #immi2에 넣는 것이 더욱 효율적일 때
        if immi2[1] > i[0]:
            # 기다리는 시간이 발생했기 때문에 그 만큼 delay 변수에 값을 넣어준다
            delay += immi2[1] - i[0]
            # immi2 변수 초기화
            immi2 = [i[0], immi2[1]+i[1]]
        else:
            # immi2 변수 초기화
            immi2 =[i[0],i[0]+i[1]]

    else:
        # immi1에 넣는 것이 더욱 효율적일 때
        if immi1[1] > i[0]:
            # 기다리는 시간이 발생했기 때문에 그 만큼 delay 변수에 값을 넣어준다
            delay += immi1[1] - i[0]
            # immi1 변수 초기화
            immi1 = [i[0],immi1[1]+i[1]]
        else:
            # immi1 변수 초기화
            immi1 = [i[0],i[0]+i[1]]

# 소수점 이하 1자리까지 출력
print(format(delay/len(list1), ".1f"))