import sys
n = int(sys.stdin.readline().strip())
list1 = [sys.stdin.readline().strip() for i in range(n)]
for i in sorted(list1):
    print(i)