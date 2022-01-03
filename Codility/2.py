def solution(message, K):
    answer = crop(message, K)
    return answer

def crop(message, K):
    split_message = message.split(" ")
    cnt = 0
    words = []
    for i in split_message:
        if (len(i) + cnt + len(words)) > K:
            break
        words.append(i)
        cnt += len(i)
    return " ".join(words)

print(solution('Tocrop or not to crop', 8))