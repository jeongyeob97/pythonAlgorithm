from collections import defaultdict

def solution(record):
    answer = decodeRecord(record)
    return answer


def decodeRecord(records):
    userDict = defaultdict(str)
    answer = []
    for record in records:
        detail = record.split(" ")
        if detail[0] == "Enter":
            userDict[detail[1]] = detail[2]
        #     answer.append(f'{userDict[id]}님이 들어왔습니다')
        # elif operation == "Leave":
        #     answer.append(f'{userDict[id]}님이 나갔습니다')
        if detail[0] == "Change":
            userDict[detail[1]] = detail[2]

    for record in records:
        detail = record.split(" ")
        if detail[0] == "Enter":
            answer.append(f'{userDict[detail[1]]}님이 들어왔습니다.')
            # print(f'{userDict[id]}님이 들어왔습니다')
        elif detail[0] == "Leave":
            answer.append(f'{userDict[detail[1]]}님이 나갔습니다.')
            # print(f'{userDict[id]}님이 나갔습니다')
    return answer

["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]
solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"])