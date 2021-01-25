def print_star(stars,e):
    if e <= 0:
        return stars
    temp_star = []
    for i in range(len(stars)*3):
        if i//len(stars) == 1:
            temp_star.append(stars[i % len(stars)] + " " * len(stars) + stars[i % len(stars)])
        else:
            temp_star.append(stars[i % len(stars)] * 3)
    return print_star(temp_star,e-1)

import sys
n = int(sys.stdin.readline())
e = 0
star = ["***", "* *", "***"]
while n != 3:
    n = n//3
    e += 1
star = print_star(star,e)
for i in star:
    print(i)

