def slope_board(temp_board, red, blue, out, cnt):
    if red == out:
        return cnt
    minimum = float('inf')
    steps = [[1,0],[-1,0],[0,1],[0,-1]]
    for i in steps:
        if temp_board[red[0]+i[0]][red[1]+i[1]] != "#":
            if ([red[0]+i[0],red[1]+i[1]] != blue) or (temp_board[blue[0]+i[0]][blue[1]+i[1]] != "#"):
                temp_board[red[0]][red[1]] = "."
                temp_board[blue[0]][blue[1]] = "."
                temp_board[red[0]+i[0]][red[1]+i[1]] = "R"
                print(blue[0] + i[0],blue[1] + i[1])
                temp_board[blue[0] + i[0]][blue[1] + i[1]] = "B"
                passing_board = temp_board[:]
                minimum = min(minimum, slope_board(passing_board,
                                                   [red[0]+i[0], red[1]+i[1]],
                                                   [blue[0]+i[0], blue[1]+i[1]],
                                                   out,
                                                   cnt+1))
    return minimum


import sys
x, y = map(int,sys.stdin.readline().split())
board, red, blue, out = [], [], [], []
for i in range(x):
    str1 = sys.stdin.readline()
    if "R" in str1:
        red = [i, str1.find("R")]
    if "B" in str1:
        blue = [i, str1.find("B")]
    if "O" in str1:
        out = [i, str1.find("O")]
    board.append(list(str1))

print(slope_board(board,red,blue,out,0))
