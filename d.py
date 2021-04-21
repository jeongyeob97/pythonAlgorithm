# def solution(s):
#     answer = len(s)
#     for i in range(len(s)):
#         index = i
#         cnt = len(s)
#         string = ""
#         stack = []
#         verify = True
#         while cnt:
#             if index >= len(s):
#                 index = 0
#             string += s[index]
#             index += 1
#             cnt -= 1
#         for i in string:
#             if i in "[({":
#                 stack.append(i)
#             else:
#                 try:
#                     character = stack.pop()
#                     if abs(ord(character) - ord(i)) > 2:
#                         verify = False
#                         answer -= 1
#                         break
#                 except:
#                     verify = False
#                     answer -= 1
#                     break
#         if verify and len(stack) > 0:
#             answer -= 1
#
#     return answer
#
# print(solution("[](){}"))







# from collections import defaultdict
# import heapq
#
#
# def solution(n, z, roads, queries):
#     answer = []
#     graph_list = [defaultdict(list) for i in range(n)]
#     nodes = []
#     for x,y,w in roads:
#         graph_list[x][y]=w
#         nodes.append(x)
#         nodes.append(y)
#     for query in queries:
#         answer.append(find(query,z,graph_list,nodes))
#
#     return answer
#
# def find(query,z, graph_list, nodes):
#     list1 = []
#     heapq.heappush(list1, (0, 0, 0))
#
#     while list1:
#         weighted, cnt, current = heapq.heappop(list1)
#         weighted = -(weighted)
#         if weighted == query:
#             return cnt
#         if weighted + z <= query:
#             heapq.heappush(list1,(-(weighted+z), cnt+1, current))
#         for node, w in graph_list[current].items():
#             if weighted + w <= query:
#                 heapq.heappush(list1, (-(weighted+w), cnt+1, node))
#         for node in list(set(nodes)-set([current]+list(graph_list[current].keys()))):
#             heapq.heappush(list1, (-(weighted), cnt+1, node))
#
#
#
#     return -1
# print(solution(5,5,[[1,2,3],[0,3,2]], [0,1,2,3,4,5,6]))


a = [-5,0,2,1,2]
# a = [0,1,0]
edges = [[0,1],[3,4],[2,3],[0,3]]
# edges = [[0,1],[1,2]]

from collections import defaultdict
from collections import deque
def solution(a, edges):
    answer = 0
    graph = defaultdict(list)

    for x,y in edges:
        graph[x].append(y)
        graph[y].append(x)

    leaves = deque()

    for i in range(len(a)):
        if len(graph[i]) == 1:
            leaves.append(i)

    while leaves:
        index = leaves.popleft()
        if a[index] == 0:
            continue
        parent = graph[index]

        answer += abs(a[index])
        if a[index] > 0:
            a[parent[0]] += a[i]
        else:
            a[parent[0]] -= a[i]

        a[index] = 0
        if parent[0] not in leaves:
            leaves.append(parent[0])

    if sum(a) == 0:
        return answer
    else:
        return -1



















print(solution(a,edges))







