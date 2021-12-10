def search(string):
    stack = []
    weight = {"(": 2, "[": 3}
    match = {")": "(", "]": "["}
    answer = 0
    depth = 1

    for i in range(len(string)):
        if string[i] in ["(", "["]:
            stack.append(string[i])
            depth *= weight[string[i]]
        else:
            if len(stack) == 0:
                return 0
            character = stack.pop()
            if ord(character) - ord(string[i]) not in [-1,-2]:
                return 0

            open = match[string[i]]
            if string[i-1] == open:
                answer += depth

            depth //= weight[open]

    if len(stack) == 0:
        return answer
    return 0





string = input()
print(search(string))
