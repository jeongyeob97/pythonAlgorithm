def solution(num):
    answer = cal(num)

    return [-1, answer][answer <= 500]


def cal(num):
    if num == 1:
        return 0

    if num % 2 == 0:
        return 1 + cal(num // 2)
    if num % 2 == 1:
        return 1 + cal(num * 3 + 1)

print(solution(6))
print(solution(16))