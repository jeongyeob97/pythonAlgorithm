def solution(citations):
    half = len(citations)//2
    answer = cal(citations, half)


    return answer

def cal(citations, half):
    for i in range(half + 1):
        h = len(citations) - i
        cnt = 0
        for j in citations:
            if h <= j:
                cnt += 1
        if cnt >= h:
            return h
    return 0

print(solution([3, 0, 6, 1, 5]))

## n