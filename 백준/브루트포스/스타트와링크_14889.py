import sys

def getPair(idx, left, aList):

    global min_value

    if left == 0:
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

        return

    for i in range(idx, n):
        if i not in aList:
            aList.append(i)
            getPair(i, left-1, aList)
            aList.pop()

if __name__ == "__main__" :
    n = int(sys.stdin.readline().rstrip())
    pList = list()
    min_value = 100 * n // 2
    for i in range(n):
        pList.append(list(map(int, sys.stdin.readline().rstrip().split())))

    getPair(0, int(n//2), [])
    print(min_value)