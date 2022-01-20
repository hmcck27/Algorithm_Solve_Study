"""

문제
바로 어제 최백준 조교가 방 열쇠를 주머니에 넣은 채 깜빡하고 서울로 가 버리는 황당한 상황에 직면한 조교들은,
702호에 새로운 보안 시스템을 설치하기로 하였다.

이 보안 시스템은 열쇠가 아닌 암호로 동작하게 되어 있는 시스템이다.

암호는 서로 다른 L개의 알파벳 소문자들로 구성되며 최소 한 개의 모음(a, e, i, o, u)과
최소 두 개의 자음으로 구성되어 있다고 알려져 있다.
또한 정렬된 문자열을 선호하는 조교들의 성향으로 미루어 보아 암호를 이루는 알파벳이 암호에서 증가하는 순서로 배열되었을 것이라고 추측된다.
즉, abc는 가능성이 있는 암호이지만 bac는 그렇지 않다.

새 보안 시스템에서 조교들이 암호로 사용했을 법한 문자의 종류는 C가지가 있다고 한다. 이 알파벳을 입수한 민식, 영식 형제는 조교들의 방에 침투하기 위해 암호를 추측해 보려고 한다. C개의 문자들이 모두 주어졌을 때, 가능성 있는 암호들을 모두 구하는 프로그램을 작성하시오.

입력
첫째 줄에 두 정수 L, C가 주어진다. (3 ≤ L ≤ C ≤ 15) 다음 줄에는 C개의 문자들이 공백으로 구분되어 주어진다. 주어지는 문자들은 알파벳 소문자이며, 중복되는 것은 없다.

출력
각 줄에 하나씩, 사전식으로 가능성 있는 암호를 모두 출력한다.

4 6
a t c i s w

acis
acit
aciw
acst
acsw
actw
aist
aisw
aitw
astw
cist
cisw
citw
istw

1. 모음 조합 고르기
2. 자음 조합 고르기
3. 모음 자음 적절히 섞기 -> 무조건 순서가 있으니 안 섞어도 된다.

"""

import sys

def divide(aList):
    list1 = list()
    list2 = list()
    for alpha in aList:
        if alpha in ['a', 'e', 'i', 'o', 'u']:
            list1.append(alpha)
        else:
            list2.append(alpha)

    return list1, list2

def getComposition(mCount, jCount):

    ## mCount개의 모음을 뽑고
    ## jCount개의 자음을 뽑아서
    ## 섞어서 출력

    getMoeumComposition(mCount, jCount, 0)

def getJaeumComposition(jCount, idx):

    # print("J  ",arrayJ)

    if jCount == len(arrayJ):
        result = arrayJ + arrayM
        result.sort()
        join = "".join(result)
        result_list.append(join)


    for i in range(idx, len(bList)):
        if bList[i] not in arrayJ:

            arrayJ.append(bList[i])
            getJaeumComposition(jCount, i)
            arrayJ.pop()

def getMoeumComposition(mCount, jCount, idx):

    # print("M  ",arrayM)

    if mCount == len(arrayM):
        getJaeumComposition(jCount, 0)

    for i in range(idx, len(aList)):
        if aList[i] not in arrayM:
            arrayM.append(aList[i])
            getMoeumComposition(mCount, jCount, i)
            arrayM.pop()


def validate(mCount, jCount):
    # print(mCount, jCount)
    if len(aList) < mCount or len(bList) < jCount:
        return False
    elif mCount < 1 or jCount < 2 :
        return False
    else :
        return True

if __name__ == "__main__":

    L, C = map(int, sys.stdin.readline().strip().split())
    aList = sys.stdin.readline().strip().split()
    aList, bList = divide(aList=aList)

    ## sort 해야함
    aList.sort()
    bList.sort()

    arrayM = list()
    arrayJ = list()

    result_list = list()

    for i in range(1, L-1):
        ## 1부터 iterate하니까 모음 먼저 픽하는 경우의 수이다.
        ## 가능한지 부터 살펴보기
        # print("1")
        if validate(i, L-i):
            # print("2")
            getComposition(i,L-i)

    result_list.sort()
    for i in result_list:
        print(i)
    print()






