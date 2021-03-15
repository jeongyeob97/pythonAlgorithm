from collections import defaultdict
import sys
a = defaultdict(int)
set1 = set()
for i in range(int(sys.stdin.readline().strip())):
    num = int(sys.stdin.readline().strip())
    set1.add(num)
    a[num]+=1

for i in sorted(set1):
    for j in range(a[i]):
        print(i)