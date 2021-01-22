def findPrime(num):
    if num == 1:
        return True
    for i in range(2,num):
        if num%i == 0:
            return False
    return True
import sys
answer = []
for i in range(int(sys.stdin.readline())):
    num = int(sys.stdin.readline())
    for j in range(num//2,1,-1):
        if (findPrime(j)) & (findPrime(num-j)):
            answer.append([j,num-j])
            break
for i in answer:
    print(*i)