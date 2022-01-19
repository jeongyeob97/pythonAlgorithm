from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)
def solution(n, m):
    graph, cheese = initializeGraphCheese(n)
    graph = initializeWhiteSpace(graph)
    answer = 0
    while len(cheese)>0:
        melted, cheese = findMelted(cheese,graph)
        graph = updateWhite(melted, graph)
        answer += 1
    return answer

def findMelted(cheese, graph):
    melted = set()
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    for(x,y) in cheese:
        cnt = 0
        for i in range(4):
            tx, ty =  dx[i]+x, dy[i]+y
            if 0 <= tx < len(graph) and 0 <= ty < len(graph[0]):
                cnt += graph[tx][ty]
            else:
                cnt += -100
        if cnt < -100:
            melted.add((x,y))
            graph[x][y] = 0

    return melted, cheese.difference(melted)

def updateWhite(melted, graph):
    visited = defaultdict(bool)

    for i in melted:
        if visited[i]:
            continue
        visited[i] = True
        graph[i[0]][i[1]] = -100
        graph, visited = recur(i, graph, visited)

    return graph


def initializeGraphCheese(n):
    graph = []
    cheese = set()
    for row in range(n):
        temp = []
        col = list(map(int, input().split()))
        for i in range(len(col)):
            if col[i] == 1:
                cheese.add((row, i))
            temp.append(col[i])
        graph.append(temp)
    return graph, cheese


def initializeWhiteSpace(graph):
    visited = defaultdict(bool)
    white = []
    for i in [0,len(graph)-1]:
        white += [(i,j) for j in range(len(graph[0]))]
    for i in [0, len(graph[0])-1]:
        white += [(j, i) for j in range(len(graph))]

    for i in white:
        if visited[i]:
            continue
        visited[i] = True
        graph[i[0]][i[1]] = -100
        graph, visited = recur(i, graph, visited)

    return graph

def recur(point, graph, visited):
    x,y = point
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    for i in range(4):
        if 0<=x+dx[i]<len(graph) and 0<=y+dy[i]<len(graph[0]) and not visited[(x+dx[i], y+dy[i])]:
            if graph[x+dx[i]][y+dy[i]] == 0:
                graph[x + dx[i]][y + dy[i]] = - 100
                visited[(x+dx[i], y+dy[i])] = True
                graph, visited = recur((x+dx[i], y+dy[i]), graph, visited)

    return graph, visited


n, m = map(int,input().split())
print(solution(n, m))
