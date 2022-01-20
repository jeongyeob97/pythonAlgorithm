import sys
def solution(m,n):
    growth = getGrowth(m, n)
    side = getSide(m)
    graph = [[1]*m for i in range(m)]

    calGraph(m, graph, growth, side)


def calGraph(m, graph, growth, side):
    for (point, weight) in zip(side, growth):
        graph[point[0]][point[1]] += weight
    print(*graph[0])
    for i in range(1,m):
        print(*([graph[i][0]] + graph[0][1:]))

def getSide(m):
    side = []
    for i in range(m-1,-1,-1):
        side.append((i,0))
    for i in range(1,m):
        side.append((0,i))
    return side

def getGrowth(m, n):
    growth = [0] * (2*m-1)
    for i in range(n):
        zero, one, two = map(int, sys.stdin.readline().split())
        for x in range(zero):
            growth[x] += 0
        for x in range(zero,zero + one):
            growth[x] += 1
        for x in range(zero + one, len(growth)):
            growth[x] += 2
    return growth

m, n = map(int,sys.stdin.readline().split())

solution(m,n)

