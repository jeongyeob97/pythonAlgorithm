m,e,d,n = map(int,input().split())

# def recur(a,k,n):
#     print(a,k,n)
#     if k == 1:
#         return a%n
#     elif k%2 == 0:
#         temp = ((a**(2/k)%n)**2) % n
#         print(temp)
#         return recur(temp,k//2,n)
#     else:
#         temp = (a*((a**(k-1)) % n)) % n
#         print(temp)
#         return recur(temp,k-1,n)

def cal(a, k, n):
    # 공식 사용
    if k == 1:
        return a%n
    elif k%2 == 0:
        return (((a**(2/k))%n)**2)%n
    else:
        return (a*(a**(k-1) % n))%n

#Me mod n 수행
c = cal(m,e,n)
#Cd mod n 수행
answer2 = cal(c,d,n)
print(c)
print(answer2)
