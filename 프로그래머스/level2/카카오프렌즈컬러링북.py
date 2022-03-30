def solution(orders, course):

    result = []
    # 모든 메뉴 구성 완료
    menuSet = set()
    for order in orders:
        for i in order:
            menuSet.add(i)
    # order set


    # 최댓값 저장용 dict()

    # 메뉴 셋을 순환을 위해서 리스트로
    menuSet = list(menuSet)
    menuSet.sort()

    # 모든 조합 재귀로 순환
    pick(menuSet,0, [], course[-1], orders, course)

    maxDict2 = dict()

    for i in course:
        maxDict2[i] = [[""], 0]
        for j in maxDict:
            if i == len(j) :
                if maxDict2[i][1] < maxDict[j]:
                    maxDict2[i][0] = [j]
                    maxDict2[i][1] = maxDict[j]
                elif maxDict2[i][1] == maxDict[j]:
                    maxDict2[i][0].append(j)

    for i in maxDict2:
        if maxDict2[i][1] > 1:
            result.extend(maxDict2[i][0])
    result.sort()

    return result

def pick(menuSet, curIndex, picked, toPick, orders, courses):

    if toPick >= 0 :
        if len(picked) in courses:
            for order in orders:
                if set(picked) <= set(order):

                    # 여기서 뭔가 결정하자.
                    # order에 조합이 존재하는 경우
                    # 여기서 count 저장해야 한다.

                    join = "".join(picked)

                    if join in maxDict:
                        # 우리가 구해야 하는 course라면
                        maxDict[join] += 1
                    else:
                        maxDict[join] = 1

        for i in range(curIndex, len(menuSet)):
            if menuSet[i] not in picked and orderCheck(orders, set(picked+[menuSet[i]])):
                picked.append(menuSet[i])
                pick(menuSet,i, picked, toPick-1, orders, courses)
                picked.pop()

def orderCheck(orders, pickedSet):
    for order in orders:
        if pickedSet <= set(order):
            return True
    return False

if __name__ == "__main__":

    # orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
    # course = [2,3,4]
    # maxDict = dict()
    # orders = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
    # course = [2,3,5]
    # maxDict = dict()
    orders = ["XYZ", "XWY", "WXA"]
    course = [2,3,4]
    maxDict = dict()


    print(solution(orders, course))