from collections import defaultdict

def solution(n):
    answer = 0
    visited_num = defaultdict(bool)
    while True:
        if n == 1:
            return answer
        n = calculate(n)
        if visited_num[n]:
            return -1
        visited_num[n] = True
        answer += 1
    return answer

def calculate(n):
    total = 0
    for num in list(map(int, str(n))):
        total += num**2
    return total






print(solution(19))