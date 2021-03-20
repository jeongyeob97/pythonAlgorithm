genre = ["A", "B", "C", "D", "E"]

genre_preference = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0}
not_opened = {"A": [], "B": [], "C": [], "D": [], "E": []}
not_finished = {"A": [], "B": [], "C": [], "D": [], "E": []}

preference = list(map(float, input().split()))
for i in range(len(genre)):
    genre_preference[genre[i]] = preference[i]

n, m = map(int, input().split())

whether_watched = [list(input()) for i in range(n)]
contents_genre = [list(input()) for i in range(n)]

for i in range(n):
    for j in range(m):
        if whether_watched[i][j] == "Y":
            not_opened[contents_genre[i][j]].append((i, j))
        elif whether_watched[i][j] == "O":
            not_finished[contents_genre[i][j]].append((i, j))

sorted_genre_preference = sorted(genre_preference.items(), key=lambda x: x[1], reverse=True)

for i in genre:
    if not_opened[i]:
        not_opened[i].sort()
    if not_finished[i]:
        not_finished[i].sort()

for i in sorted_genre_preference:
    type, rate = i
    if not_opened[type]:
        answer = []
        for j in not_opened[type]:
            print(type, rate, *j)

for i in sorted_genre_preference:
    type, rate = i
    if not_finished[type]:
        for j in not_finished[type]:
            print(type, rate, *j)
