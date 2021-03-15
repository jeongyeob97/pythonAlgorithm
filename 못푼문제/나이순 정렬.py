from collections import defaultdict
import sys
a = defaultdict(list)
age_list = set()
for i in range(int(sys.stdin.readline().strip())):
    age, name = sys.stdin.readline().split()
    a[int(age)].append(name)
    age_list.add(int(age))

for i in sorted(age_list):
    for j in a[i]:
        print(i, end =" ")
        print(j)

