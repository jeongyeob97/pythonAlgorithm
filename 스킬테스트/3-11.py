def solution(n):
    answer = []
    recur(1,3,2,n,answer)
    return answer

def recur(start, to, mid, n, answer):
    if n == 1:
        answer.append([start,to])
        return
    recur(start, mid, to, n - 1, answer)
    answer.append([start, to])
    recur(mid, to, start, n - 1, answer)




# 하노이탑 구현하기 얼마나 발전했을지 우리한번 알아보아요

print(solution(4))