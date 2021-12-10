def solution(p):
    if isComplete(p):
        return p

    if p == "":
        return ""
    parenDict = {"(": 0, ")": 0}
    answer = ''

    for i in range(len(p)):
        answer += p[i]
        parenDict[p[i]] += 1
        if parenDict["("] == parenDict[")"]:
            if isComplete(answer):
                return answer + solution(p[i + 1:])
            return "(" + solution(p[i + 1:]) + ")" + transform(answer)

    return ""


def transform(text):
    # while True:
    text = "".join([["(",")"][i=="("]  for i in text[1:-1]])
    # text = "".join(reversed(text[1:-1]))
    return text


def isComplete(text):
    stack = []
    for i in text:
        if len(stack) == 0:
            stack.append(i)
        elif ord(stack[-1]) - ord(i) == -1:
            stack.pop()
        else:
            stack.append(i)

    return [False, True][len(stack) == 0]




print(solution("(()())()"))
print(solution(")("))
print(solution("()))((()"))
print(solution(")()()))((("))

print(solution(")()(()"))