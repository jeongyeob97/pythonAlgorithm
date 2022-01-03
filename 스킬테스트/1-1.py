def solution(arr):
    answer = [arr[0]]
    currentNum = arr[0]

    for i in range(1, len(arr)):
        if arr[i] != currentNum:
            answer.append(arr[i])
            currentNum = arr[i]

    if currentNum != answer[-1]:
        answer.append(currentNum)

    return answer