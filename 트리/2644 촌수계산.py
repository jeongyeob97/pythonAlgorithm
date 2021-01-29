# from collections import defaultdict
#
# class FamilyTree:
#     def __init__(self):
#         self._nodeDict = defaultdict(int)
#
#     def addNodes(self, parent, child):
#         if self._nodeDict[parent] == 0:
#             parent_node = self.Node(parent)
#             child_node = self.Node(child)
#             parent_node._children[child], child_node._parent[parent] = child_node, parent_node
#             self._nodeDict[child], self._nodeDict[parent] = child_node, parent_node
#         else:
#             parent_node = self._nodeDict[parent]
#             child_node = self.Node(child)
#             parent_node._children[child], child_node._parent[parent] = child_node, parent_node
#             self._nodeDict[child] = child_node
#
#     class Node:
#         def __init__(self, element):
#             self._parent = defaultdict(int)
#             self._element = element
#             self._children = defaultdict(int)
#
# def recur(node, need_element, cnt):
#     if (need_element in node._parent) or (need_element in node._children):
#         return cnt+1
#     print(node._parent)
#     print(node._children)
#     visitied[node._element] = 1
#     accessibleList = list(node._children) + list(node._parent)
#     for i in accessibleList:
#         if visitied[i] == 0:
#             return recur(family_tree._nodeDict[i], need_element, cnt+1)
#
# input()
# x,y = map(int,input().split())
# family_tree = FamilyTree()
# visitied = defaultdict(int)
# for i in range(int(input())):
#     parent, child = map(int,input().split())
#     family_tree.addNodes(parent,child)
#
# print(recur(family_tree._nodeDict[x],y,0))

# import sys
# from collections import defaultdict
# sys.setrecursionlimit(10**6)
# input()
# dict1 = defaultdict(list)
# visited = []
# x, y = map(int,input().split())
# for i in range(int(input())):
#     parent, child = map(int,input().split())
#     dict1[parent].append(child)
#     dict1[child].append(parent)
#
# def recur(cnt, accesible, y):
#     tempList = []
#     for i in accesible:
#         if i in visited:
#             continue
#         if y in dict1[i]:
#             return cnt + 1
#         visited.append(i)
#         tempList += dict1[i]
#     return recur(cnt+1, tempList,y)
#
# visited.append(x)
# print(recur(1,dict1[x],y))


def bfs(current, goal):
    cnt = 0
    bfs_list = deque([[current,cnt]])

    while bfs_list:
        node, count = bfs_list.popleft()
        visited[node] = True
        for i in family_tree[node]:
            if visited[i]:
                continue
            if i == goal:
                return count + 1
            bfs_list.append([i,count+1])
    return -1



from collections import defaultdict,deque
num = int(input())
x,y = map(int,input().split())
visited = [False] * (num+1)
family_tree = defaultdict(list)
for i in range(int(input())):
    parent, child = map(int,input().split())
    family_tree[parent].append(child)
    family_tree[child].append(parent)

print(bfs(x,y))
