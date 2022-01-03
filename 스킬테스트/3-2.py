import re

def solution(user_id, banned_id):
    temp_user_id = []
    answer = 0
    for i in banned_id:
        temp = verify(user_id, i)
        if temp:
            temp_user_id.append(temp)
    temp = recur(temp_user_id, 0 ,[])
    print(temp)

    return answer

def verify(user_id, banned_id):
    regex = re.compile("^"+banned_id.replace("*", "[a-zA-Z]")+"$")
    temp = []
    cnt = 0
    for i in user_id:
        if regex.match(i):
            temp.append(i)
    return temp

# def calCombination(user_id):


def recur(user_id, index, list1):
    if index <= len(user_id):
        return list1
    temp = []
    for i in user_id[index]:
        temp.append(recur(user_id, index + 1, list1 + [i]))
    return temp

print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]	))