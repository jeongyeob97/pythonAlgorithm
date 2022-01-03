def solution(n):
    answer = 0
    answer = cal(n) % 1234567
    return answer


def cal(maximum):
    if maximum == 1:
        return 1
    step_list = [0] * maximum
    step_list[0], step_list[1] = 1, 1

    for i in range(1, maximum):
        step_list[i] += step_list[i-1]

        if i - 2 < 0:
            continue
        step_list[i] += step_list[i-2]

    return step_list[-1]
