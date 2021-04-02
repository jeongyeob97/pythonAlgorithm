n = int(input())
list1 = []
cnt, delay = 0, 0
immi1, immi2 = [0, 0], [0, 0]

for i in range(n):
    a,b = map(int,input().split())
    cnt += a
    list1.append([cnt,b])

for i in list1:
    if immi1[1] > immi2[1]:
        if immi2[1] > i[0]:
            delay += immi2[1] - i[0]
            immi2 = [i[0], immi2[1]+i[1]]
        else:
            immi2 =[i[0],i[0]+i[1]]

    else:
        if immi1[1] > i[0]:
            delay += immi1[1] - i[0]
            immi1 = [i[0],immi1[1]+i[1]]
        else:
            immi1 = [i[0],i[0]+i[1]]

print(format(delay/len(list1), ".1f"))