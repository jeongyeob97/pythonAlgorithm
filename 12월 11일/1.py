def solution(arr):
    answer = 0
    cnt = 0
    for i in arr:
        cnt += i
        if cnt >= 0:
            answer += 1
    return answer

print(solution([ 5, 2, -16, 4 ]	))