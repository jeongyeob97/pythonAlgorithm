def c_function(x,num):
    permutation[int(x)-1] = int(num)

def p_function(x1, x2):
    num = 1
    for i in range(int(x1)-1,int(x2)):
        num *= permutation[i]
    return num

def verification(num):
    if num == 0:
        return "0"
    elif num > 0:
        return "+"
    else:
        return "-"

import sys
import math
input = sys.stdin.readline
while True:
    try:
        n, r = map(int, input().split())
        permutation = list(map(int, input().split()))
        expo = math.ceil(math.log2(len(permutation)))
        tree = [float('inf')] * (2**expo)
        start = (2**(expo-1))+1
        for i in range(len(permutation),0,-1):
            if i*2 == len(tree) - start:
                tree[start//2] = permutation[len(permutation)-i+1]
                start += 2
            else:
                tree[start] = permutation[len(permutation)-i+1]
                start += 1
        answer = ""
        for i in range(r):
            oper, n1, n2 = input().split()
            if oper == "C":
                c_function(n1, n2)
            else:
                answer += verification(p_function(n1, n2))

        print(answer)

    except Exception:
        break