## 일단 이중 리스트를 만들자

def solution(pixels):
    answer = ''
    for index in range(0,len(pixels[0]), 3):
        answer += define(index, pixels)


    return answer

def define(index, pixels):
    if pixels[0][index:index+3] == "111":
        if pixels[2][index:index+3] != "111":
            if pixels[3][index] == "1":
                return "0"
            else:
                return "7"

        temp = ""
        for i in range(5):
            temp += pixels[i][index+2]

        if temp == "11111":
            if (pixels[1][index] == "0") and (pixels[3][index] == "0"):
                return "3"
            elif (pixels[3][index] == "0"):
                return "9"
            else:
                return "8"

        if (pixels[1][index+2] == "0") and (pixels[3][index] == "0"):
            return "5"
        elif pixels[1][index+2] == "0":
            return "6"
        else:
            return "2"
    if pixels[4][index: index+3] == "111":
        return "1"
    else:
        return "4"

print(solution(["111111111111111111111111110111111111","001101001101101100101101010101001100","111101111101101111101111010111111111","100101100101101101101001010101001001","111111111111111111111111111111111111"]))
print(solution(["110111101111111111110111","010101101100101101010100","010111111111101111010111","010001001001101101010001","111111001111111111111111"]	))
print(solution(["111110111101111101111101111","100010101101001101100101101","111010111111111111111111001","001010101001100001001001001","111111111001111001111001001"]	))