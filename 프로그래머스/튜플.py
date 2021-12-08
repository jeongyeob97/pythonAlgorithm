def solution(s):
    text = s[1:-1].replace("}", "").replace(",{","|").replace("{", "")
    tuple = sorted([list(map(int,i.split(","))) for i in text.split("|")], key = lambda x: len(x))
    temp = set()
    answer = []
    for i in tuple:
        answer.append(list(set(i) - temp)[0])
        temp = set(i)

    return answer


# print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
# print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))
print(solution("{{20,111},{111}}"))
print(solution("{{123}}"))
# print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))

