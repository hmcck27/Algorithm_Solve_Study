## 비밀지도

def solution(n, arr1, arr2):
    answer = []
    for one, two in zip(arr1, arr2):

        bit = bin(one | two)
        temp = ""
        bitMoveCount = n - len(bit) + 2
        for i,s in enumerate(bit):
            # 시작
            if i == 0 or i == 1:
                continue
            if s == '0':
                temp += " "
            else:
                temp += "#"

        for i in range(bitMoveCount):
            temp = " " + temp
        answer.append(temp)
    return answer

def solution2(n, arr1, arr2):
    answer = []
    for one, two in zip(arr1, arr2):
        one_two = one | two

        bitStr = bin(one_two)[2:]
        print(bitStr)
        bitStr = bitStr.replace("0", " ")
        bitStr = bitStr.replace("1", "#")
        bitStr = bitStr.rjust(n, ' ')
        answer.append(bitStr)

    print(answer)
    return answer


if __name__ == "__main__":

    n = 6
    arr1 = [46, 33, 33, 22, 31, 50]
    arr2 =[27, 56, 19, 14, 14, 10]

    # n = 5
    # arr1 = [9, 20, 28, 18, 11]
    # arr2 = [30, 1, 21, 17, 28]

    solution2(n, arr1, arr2)
