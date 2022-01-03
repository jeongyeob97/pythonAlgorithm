def solution(scores):
    answer = 0
    weight = {"A": 5, "B": 4, "C": 3, "D": 2, "E":1, "F":0}
    for i in scores:
        answer += defineScore(i, weight)

    return answer

def defineScore(score, weight):
    A_count, F_count, total = 0, 0, 0
    maximum, minimum = min(score), max(score)

    for element in score:
        if element == "A":
            A_count += 1
        if element == "F":
            F_count += 1
        total += weight[element]

        if F_count >= 2:
            return 0

    if (A_count >= 2) or (total - weight[maximum] - weight[minimum]) / (len(score)-2) >= 3:
        return 1

    return 0

print(solution(["AAFAFA", "FEECAA", "FABBCB", "CBEDEE", "CCCCCC"]))
print(solution(["BCD", "ABB","FEE"]))