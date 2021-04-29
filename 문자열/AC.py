from collections import deque

def execute(array, instruction):
    if array == [""]:
        temp_array = deque()
    else:
        temp_array = deque(array)
    verify = True
    i = 0
    while i < len(instruction):
        if instruction[i] == "R":
            verify = not verify
        else:
            if len(temp_array) == 0:
                print("error")
                return
            if verify:
                temp_array.popleft()
            else:
                temp_array.pop()
        i += 1
    if verify:
        answer = list(temp_array)
    else:
        answer = list(reversed(temp_array))

    print("["+",".join(answer)+"]")
    return




for i in range(int(input())):
    instruction = input()
    array_len = int(input())
    array = input().replace("[","").replace("]","").split(",")
    execute(array, instruction)



