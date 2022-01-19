import sys

def getPair(idx, aList):

    global min_value

    aTeamScore = 0
    bTeamScore = 0
    bList = []

    for i in range(n):
        if i not in aList:
            bList.append(i)

    for i in aList:
        for j in aList:
            aTeamScore += pList[i][j]

    for i in bList:
        for j in bList:
            bTeamScore += pList[i][j]

    if abs(aTeamScore - bTeamScore) < min_value:
        min_value = abs(aTeamScore - bTeamScore)

    for i in range(idx, n):
        if i not in aList:
            aList.append(i)
            getPair(i, aList)
            aList.pop()

if __name__ == "__main__" :
    n = int(sys.stdin.readline().rstrip())
    pList = list()
    min_value = 100 * n // 2
    for i in range(n):
        pList.append(list(map(int, sys.stdin.readline().rstrip().split())))

    getPair(0, [])
    print(min_value)