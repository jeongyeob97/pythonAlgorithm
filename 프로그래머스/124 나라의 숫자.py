def solution(n):
    trinary = ["1","2","4"]
    if n <= 3:
        return trinary[n-1]
    div, mod = divmod(n-1,3)

    return solution(div) + trinary[mod]


print(solution(1))
print(solution(4)) #11
print(solution(8)) #22
print(solution(10)) #41