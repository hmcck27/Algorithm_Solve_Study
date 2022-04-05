def solution(info, query):
    answer = []

    # 처음에 info를 읽으면서 최대한 효율적인 자료구조로 작성이 마무리되야 한다.
    infoDict = dict()
    scoreDict = dict()
    for i, oneInfo in enumerate(info):
        info_split = oneInfo.split(" ")
        for j in info_split[:-1]:
            if j not in infoDict.keys():
                infoDict[j] = set([i])
            else:
                infoDict[j].add(i)
        scoreDict[i] = int(info_split[-1])

    initSet = set([i for i in range(i+1)])

    for oneQuery in query:
        splitQuery = oneQuery.split(" ")
        count = 0
        conScore = int(splitQuery[-1])
        tempSet = initSet

        for info in splitQuery[:-1]:
            if info == "and" :
                continue
            elif info == "-":
                continue
            else:
                tempSet = tempSet & infoDict[info]
        for el in tempSet:
            if scoreDict[el] >= conScore:
                count += 1
        answer.append(count)


    return answer

if __name__ == "__main__":

    info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
    query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
    print(solution(info, query))
