n = int(input())
time_list = []
start_time = "00:00"
end_time = "24:00"
verification = True
for i in range(n):
    temp = input().replace(" ","")
    temp = temp.split("~")
    if temp[0] > start_time:
        start_time = temp[0]
    if temp[1] < end_time:
        end_time = temp[1]
    time_list.append(temp)

for i in range(n):
    if time_list[i][0] > end_time or time_list[i][1] < start_time:
        verification = False
        break

if verification:
    print(start_time + " ~ " + end_time)
else:
    print(-1)