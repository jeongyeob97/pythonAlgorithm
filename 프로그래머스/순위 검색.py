def solution(info, query):
    answer = []
    info_list = [i.split() for i in info]
    for temp in query:
        answer.append(categorizeInfo(info_list, defineQuery(temp)))
    return answer

def defineQuery(query):
    query_list = query.split()
    extract = []
    for i in range(0, len(query_list)-1, 2):
        extract.append(query_list[i])
    extract.append(query_list[-1])
    return extract

def categorizeInfo(infos, query):
    cnt = 0
    for info in infos:
        x = query[0]
        y = info[0]
        if not ((query[0] == info[0]) or (query[0] == "-")):
            continue
        if not ((query[1] == info[1]) or (query[1] == "-")):
            continue
        if not ((query[2] == info[2]) or (query[2] == "-")):
            continue
        if not ((query[3] == info[3]) or (query[3] == "-")):
            continue
        if not ((int(query[4]) <= int(info[4])) or (query[4] == "-")):
            continue
        cnt += 1

    return cnt

def categorize

print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],
               ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))