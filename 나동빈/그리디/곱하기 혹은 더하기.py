list1 = list(input())
sum = [int(list1[0]),1][int(list1[0]) == 0]
for i in range(1,len(list1)):
    if int(list1[i]) > 1:
        sum *= int(list1[i])
    else:
        sum += int(list1[i])
print(sum)
