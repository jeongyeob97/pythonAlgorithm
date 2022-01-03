from itertools import combinations

def solution(graph, n):
    teacher, empty = getPosition(graph, n)
    available = False

    for pos in combinations(empty, 3):
        if checkStatus(pos, graph, teacher):
            available = True
            break

    return ["NO", "YES"][available]

def getPosition(graph,n):
    teacher = []
    empty = []
    for x in range(n):
        for y in range(n):
            if graph[x][y] == "T":
                teacher.append((x, y))
            elif graph[x][y] == "X":
                empty.append((x, y))
    return teacher, empty

def checkStatus(pos, graph, teacher):
    convertGraph(pos, graph, True)

    for (x,y) in teacher:
        if not verify(x,y,graph,False, False):
            convertGraph(pos, graph, False)
            return False
        if not verify(x, y, graph, True, False):
            convertGraph(pos, graph, False)
            return False
        if not verify(y, x, graph, False, True):
            convertGraph(pos, graph, False)
            return False
        if not verify(y, x, graph, True, True):
            convertGraph(pos, graph, False)
            return False
    convertGraph(pos, graph, False)
    return True


def verify(change, fixed, graph, isNegative, isRow):
    if isNegative:
        if isRow:
            for i in range(change-1, -1, -1):
                if graph[fixed][i] == "O":
                    return True
                elif graph[fixed][i] == "S":
                    return False
        else:
            for i in range(change-1, -1, -1):
                if graph[i][fixed] == "O":
                    return True
                elif graph[i][fixed] == "S":
                    return False

        return True

    if isRow:
        for i in range(change + 1, len(graph)):
            if graph[fixed][i] == "O":
                return True
            elif graph[fixed][i] == "S":
                return False
    else:
        for i in range(change + 1, len(graph)):
            if graph[i][fixed] == "O":
                return True
            elif graph[i][fixed] == "S":
                return False

    return True



def convertGraph(pos, graph, isChanging):
    if isChanging:
        for (x, y) in pos:
            graph[x][y] = "O"
        return
    for (x,y) in pos:
        graph[x][y] = "X"


n = int(input())
graph = [input().split(" ") for i in range(n)]
print(solution(graph, n))