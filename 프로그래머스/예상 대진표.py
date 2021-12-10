def solution(n,a,b):
    big, small = max(a,b), min(a,b)
    repeat = recur(1, n, small,big, 0)
    num = n//(2**repeat)
    answer = count(num)
    return answer

def recur(min,max, a, b, cnt):
    num = (min+max)//2
    if a<=num & num < b:
        return cnt
    elif a <= num and b <= num:
        return recur(min, num, a,b, cnt + 1)
    else:
        return recur(num+1, max, a, b, cnt + 1)

def count(number):
    cnt = 0
    while number != 1:
        number//=2
        cnt+=1
    return cnt

print(solution(8,4,7))

print(solution(16,3,7))

