def solution(s):
    stack = []
    index = 0
    while index < len(s):
        if not stack or stack[-1] != s[index]:
            stack.append(s[index])
        elif stack[-1] == s[index]:
            stack.pop()
        index += 1

    return [1,0][len(stack) > 0]


print(solution("baabaa"))
print(solution("cdcd"))

