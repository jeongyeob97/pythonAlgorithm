from itertools import combinations

def solution(relation):
    answer = 0
    permutation_list = createCombination(len(relation[0]))
    for tuple in permutation_list:
        answer += start(tuple, relation)

    return answer


def createCombination(length):
    temp = []
    for i in range(length):
        temp += list(combinations(range(length), i))
    return temp


def start(tuple, relation):
    array = list(tuple)
    temp = [[relation[j][i] for i in array] for j in range(len(relation))]

    temp = list(map(convertTuple, temp))

    if len(set(temp)) != len(relation):
        return False
    elif len(array) == 1:
        return True

    return trasverse(tuple, relation, True)


def convertTuple(list):
    return tuple(list)


def trasverse(tuple, relation, isFirst):
    array = list(tuple)
    temp = [[relation[j][i] for i in array] for j in range(len(relation))]
    returnValue = True

    temp = list(map(convertTuple, temp))

    if (len(set(temp)) == len(relation)) & (isFirst == False):
        return False

    if len(tuple) == 1:
        return True

    for i in range(len(tuple)):
        returnValue &= trasverse(tuple[:i] + tuple[i + 1:], relation, False)
    return returnValue


print(solution([["100", "ryan", "music", "2"], ["200", "apeach", "math", "2"], ["300", "tube", "computer", "3"],
                ["400", "con", "computer", "4"], ["500", "muzi", "music", "3"], ["600", "apeach", "music", "2"]]))


## dictionary [String: Bool]
