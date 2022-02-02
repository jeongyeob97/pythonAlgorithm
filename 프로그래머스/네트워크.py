from collections import defaultdict,deque

def solution(n, computers):
    answer = 0
    graph = makeGraph(n, computers)
    answer = countNetwork(n, graph)
    return answer

def makeGraph(n, computers):
    graph = defaultdict(list)
    for i in range(n):
        for idx in range(len(computers[i])):
            if computers[i][idx] == 1:
                graph[i].append(idx)

    return graph

def countNetwork(n, graph):
    isVisited = defaultdict(bool)
    cnt = 0
    for i in range(n):
        if isVisited[i]:
            continue
        queue = deque([i])

        while queue:
            idx = queue.popleft()
            isVisited[idx] = True

            for node in graph[idx]:
                if isVisited[node]:
                    continue
                queue.append(node)
        cnt += 1

    return cnt





print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))