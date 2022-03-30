import re
def solution(dartResult):

    search = re.findall('[0-9]+[SDT][*#]?', dartResult)
    answerList = []
    for temp in search:
        score = int(re.search('[0-9]+', temp).group())
        bonus = re.search('[SDT]', temp).group()
        if bonus == 'D':
            score = score ** 2
        elif bonus == 'T':
            score = score ** 3
        option = re.search('[*#]', temp)

        if option:
            if option.group() == '*':
                score = 2 * score
                if len(answerList) >= 1:
                    answerList[-1] = 2 * answerList[-1]
            else:
                score = -score

        answerList.append(score)

    result = 0
    for answer in answerList:
        result += answer

    return result

if __name__ == "__main__":

    dartResult = "1S2D*3T"
    dartResult = "1D2S#10S"
    print(solution(dartResult))
