def solution(s):
    answer = 0

    # 전체 문자열의 절반까지만 보면 된다.
    min = len(s)
    for i in range(1, len(s)//2 + 1):
        parsed = parseString(s, i)

        # print(parsed)
        if min > parsed:
            min = parsed

    return min


def parseString(original, parse):
    # original 문자열을 parse 단위로 잘라서 파싱된 문자열을 반환하다.

    parseList = []
    # 1. 전체 문자열을 단위수로 split한다.
    for i in range(len(original)):
        if i % parse == 0:
            # 시작 지점이면 그냥 append
            parseList.append(original[i])
        else:
            parseList[-1] += original[i]

    # print(parseList)

    start = parseList[0]
    strList = []
    countList = []
    strList.append(start)
    countList.append(1)
    count = 1
    for i in range(1, len(parseList)):
        if parseList[i] == start:
            countList[-1] += 1
        else:
            start = parseList[i]
            strList.append(parseList[i])
            countList.append(count)
            count = 1


    len1 = len("".join([str(count) for count in countList if count != 1 ]))
    len1 += len("".join(list(strList)))


    # print(list(map(str, countList)))
    # print(list(strList))
    # print("len : ", len1)

    return len1


if __name__ == "__main__":
    s = "aabbaccc"
    s = "ababcdcdababcdcd"
    s = "abcabcabcabcdededededede"
    print(solution(s))