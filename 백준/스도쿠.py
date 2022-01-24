def solution(sudoku, emtpy):
    dfs(sudoku,empty,0)
    for line in sudoku:
        print(*line)


def dfs(sudoku, empty, index):
    if index >= len(empty):
        return True

    available = findAvailable(empty[index], sudoku)

    x,y = empty[index]

    if len(available) == 0:
        return False

    while available:
        num = available.pop()
        sudoku[x][y] = num
        if dfs(sudoku, empty, index+1):
            return True
        sudoku[x][y] = 0

    return False


def findAvailable(point, sudoku):
    x,y = point
    candidates = set([1,2,3,4,5,6,7,8,9])
    using = set()

    for i in range(9):
        if sudoku[x][i] != 0:
            using.add(sudoku[x][i])

        if sudoku[i][y] != 0:
            using.add(sudoku[i][y])

    tx = (x//3) * 3
    ty = (y//3) * 3

    for i in range(tx, tx+3):
        for j in range(ty, ty+3):
            if sudoku[i][j] != 0:
                using.add(sudoku[i][j])

    return candidates.difference(using)

import sys
input = sys.stdin.readline
sudoku = []
empty = []

for i in range(9):
    line = list(map(int, input().split()))
    temp = []
    for idx in range(len(line)):
        num = line[idx]
        if num == 0:
            empty.append((i, idx))
        temp.append(num)
    sudoku.append(temp)
solution(sudoku,empty)