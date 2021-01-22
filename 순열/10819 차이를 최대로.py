import sys
import itertools
input()
num_list, maximum = list(map(int,sys.stdin.readline().split())), 0
for i in itertools.permutations(num_list,len(num_list)):
    sum = 0
    for j in range(0,len(i)-1):
        sum += abs(i[j]-i[j+1])
    maximum = [sum,maximum][maximum >= sum]
print(maximum)