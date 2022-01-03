def solution(skill, skill_trees):
    answer = 0
    for skill_tree in skill_trees:
        answer += compare(skill, skill_tree)

    return answer

def compare(skill, skill_tree):
    dictionary = { skill_tree[i]: False for i in range(len(skill_tree)) }
    dictionary.update({skill[i]: i+1 for i in range(len(skill))})
    skill_count = 0

    for i in skill_tree:
        if dictionary[i]:
            if abs(dictionary[i] - skill_count) == 1:
                skill_count = dictionary[i]
            else:
                return 0
    return 1


print(solution("CBD",["BACDE", "CBADF", "AECB", "BDA"] ))