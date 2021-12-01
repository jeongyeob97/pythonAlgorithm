def solution(s):
    answer = len(s)
    for i in range(1,len(s) - 1):
        answer = min(zipString(s, i), answer)
    return answer

def zipString(text, interval):
    answer, index, count = 0, 0, 0
    while index < len(text):
        temp = text[index: index + interval]
        if temp == text[index + interval: (index + interval + interval)]:
            count += 1
        else:
            if count > 0:
                answer += len(str(count + 1)) + len(temp)
            else:
                answer += interval
            count = 0
        index += interval
    answer += len(text) - index
    return answer