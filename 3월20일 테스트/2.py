n = int(input())
route = list(input())
cases = [0] * len(route)
cases[0] = 1

for i in range(n-1):
    if route[i] == "0":
        continue
    if i+2 <= n-1:
        cases[i+2] += cases[i]
    if i+1 <= n-1:
        cases[i+1] += cases[i]

print(cases[-1])