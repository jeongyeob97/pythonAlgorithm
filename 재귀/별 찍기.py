def print_star(stars):
    temp_star = []
    for i in range(len(stars)*3):
        if i//len(stars) == 1:
            temp_star.append(stars[i % len(stars)] + " " * len(stars) + stars[i % len(stars)])
        else:
            temp_star.append(stars[i % len(stars)] * 3)
    return temp_star

import sys
n = int(sys.stdin.readline())
e = 0
star = ["***", "* *", "***"]
while n != 3:
    n = n//3
    e += 1
for i in range(e):
    star = print_star(star)
for i in star:
    print(i)



