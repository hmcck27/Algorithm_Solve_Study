import sys

def printArray(array):
    for i in range(len(array)):
        for j in range(len(array[i])):
            print(array[i][j], end=" ")
        print()

def operationOne(n,m,array):
    # 상하 반전
    newArray = list()
    for i in range(n):
        newArray.append(array[n-i-1])
    return newArray

def operationTwo(n,m,array):
    # 좌우 반전
    newArray = [[0 for i in range(m)] for j in range(n)]
    for i in range(n):
        for j in range(m):
            newArray[i][j] = array[i][m-j-1]

    return newArray

def operationThree(n,m,array):
    # 오른쪽으로 90도 회전 연산
    # col은 위치만 row로 이동
    # row는 col의 n- 로 이동
    newArray = [[0 for i in range(n)] for j in range(m)]
    for i in range(n):
        for j in range(m):
            newArray[j][n-i-1] = array[i][j]
    return newArray

def operationFour(n,m,array):
    # 왼쪽으로 90도 회전 연산
    # n-col 이 row로 이동
    # row는 col로 이동
    newArray = [[0 for i in range(n)] for j in range(m)]
    for i in range(n):
        for j in range(m):
            newArray[m-j-1][i] = array[i][j]

    return newArray

def operationFive(n,m,array):
    # 시계방향 이동
    # 1 -> 2, 2 -> 3, 3 -> 4, 4 -> 1
    divedArray = divFour(n,m,array)
    newDivedArray = [divedArray[3], divedArray[0], divedArray[1], divedArray[2]]
    combedArray = combFour(n,m,newDivedArray)
    return combedArray

def operationSix(n,m,array):
    # 반시계방향 이동
    # 1 -> 4, 2 -> 1, 3 -> 2, 4 -> 3
    divedArray = divFour(n, m, array)
    newDivedArray = [divedArray[1], divedArray[2], divedArray[3], divedArray[0]]
    combedArray = combFour(n, m, newDivedArray)
    return combedArray

def combFour(n,m,divArray):
    newArray = [[0 for i in range(m)] for j in range(n)]

    for k,tempList in zip([[0, 0], [0, m // 2], [n // 2, m // 2], [n // 2, 0]], divArray):
        for i in range(n//2):
            for j in range(m//2):
                newArray[k[0] + i][k[1] + j] = tempList[i][j]
    return newArray

def divFour(n,m,array):
    divArray = []
    for k in [[0,0],[0,m//2],[n//2,m//2], [n//2,0]]:
        temp = []
        for i in range(n//2):
            temp2 = []
            for j in range(m//2):
                temp2.append(array[k[0] + i][k[1] + j])
            temp.append(temp2)
        divArray.append(temp)


    # for k in divArray:
    #     printArray(k)
    return divArray


if __name__ == "__main__":
    n,m,o = map(int, sys.stdin.readline().split())
    array = list()
    for _ in range(n):
        array.append(list(map(int, sys.stdin.readline().split())))
    on = list(map(int, sys.stdin.readline().split()))

    for num in on:
        if num == 1:
            array = operationOne(n,m,array)
        elif num == 2:
            array = operationTwo(n,m,array)
        elif num == 3:
            array = operationThree(n,m,array)
            temp = n
            n = m
            m = temp
        elif num == 4:
            array = operationFour(n,m,array)
            temp = n
            n = m
            m = temp
        elif num == 5:
            array = operationFive(n,m,array)
        elif num == 6:
            array = operationSix(n,m,array)

    printArray(array)

