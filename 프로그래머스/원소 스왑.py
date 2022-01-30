from itertools import permutations

def solution(numbers, K):
    answer = float('inf')
    possible = findAvailable(numbers, K)
    if len(possible) == 0:
        answer = -1
        return answer
    for candidate in possible:
        answer = min(answer, countSwap(numbers, candidate))
    return answer

def findAvailable(numbers, K):
    possible = []
    for permutation in map(list,permutations(numbers, len(numbers))):
        accumulate = permutation[0]
        flag = True
        for idx in range(1, len(permutation)):
            if abs(accumulate - permutation[idx]) > K:
                flag = False
                break
            accumulate = permutation[idx]
        if flag:
            possible.append(permutation)
    return possible

def countSwap(numbers, candidates):
    index_dict = {candidates[i]: i for i in range(len(candidates))}
    cnt = 0
    for idx in range(len(candidates)):
        if numbers == candidates:
            break

        if numbers[idx] != candidates[idx]:
            candidates, index_dict = swap(numbers, candidates, index_dict, idx)
            cnt += 1
    return cnt

def swap(numbers, candidates, index_dict, idx):
    candidates_num, numbers_num = candidates[idx], numbers[idx]
    swapping_idx = index_dict[numbers_num]

    candidates[idx] = numbers_num
    candidates[swapping_idx] = candidates_num
    index_dict[numbers_num] = index_dict[candidates_num]
    index_dict[candidates_num] = swapping_idx

    return candidates, index_dict


print(solution([10, 40, 30, 20], 20))
print(solution([3, 7, 2, 8, 6, 4, 5, 1], 3))