
def solution(phone_numbers, phone_owners, number):
    answer = match(phone_numbers, phone_owners, number)
    return answer

def match(phone_numbers, phone_owners, number):
    phone_numbers_dict = {phone_numbers[i]: i for i in range(len(phone_numbers))}
    if number in phone_numbers_dict:
        index = phone_numbers_dict[number]
        return phone_owners[index]
    return number


print(solution(
["234-567-890"],
["harry"],
"444-444-454"
))