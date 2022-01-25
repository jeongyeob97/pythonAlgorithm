from collections import defaultdict, deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

truth = []
for i in list(map(int,input().split()))[1:]:
    truth.append(i)

visited_parties = defaultdict(list)
parties = []
for i in range(m):
    temp = list(map(int,input().split()))[1:]
    for ppl in temp:
        visited_parties[ppl].append(i)
    parties.append(temp)

truth_parties = defaultdict(bool)
cnt = 0
queue = deque(truth)

while queue:
    ppl = queue.popleft()
    for party in visited_parties[ppl]:
        if truth_parties[party]:
            continue
        truth_parties[party] = True
        cnt += 1
        queue += parties[party]

print(m-cnt)