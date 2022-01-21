def solution(num_list):
    standard = 1
    for i in num_list:
        if standard < i:
            break
        standard += i
    return standard
n = int(input())
num_list = list(map(int,input().split()))
print(solution(sorted(num_list)))

