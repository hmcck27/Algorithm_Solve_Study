"""

문제
상근이는 어렸을 적에 "봄보니 (Bomboni)" 게임을 즐겨했다.

가장 처음에 N×N크기에 사탕을 채워 놓는다. 사탕의 색은 모두 같지 않을 수도 있다.
상근이는 사탕의 색이 다른 인접한 두 칸을 고른다.
그 다음 고른 칸에 들어있는 사탕을 서로 교환한다.
이제, 모두 같은 색으로 이루어져 있는 가장 긴 연속 부분(행 또는 열)을 고른 다음 그 사탕을 모두 먹는다.

사탕이 채워진 상태가 주어졌을 때, 상근이가 먹을 수 있는 사탕의 최대 개수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 보드의 크기 N이 주어진다. (3 ≤ N ≤ 50)

다음 N개 줄에는 보드에 채워져 있는 사탕의 색상이 주어진다. 빨간색은 C, 파란색은 P, 초록색은 Z, 노란색은 Y로 주어진다.

사탕의 색이 다른 인접한 두 칸이 존재하는 입력만 주어진다.

출력
첫째 줄에 상근이가 먹을 수 있는 사탕의 최대 개수를 출력한다.

예제 입력 1
3
CCP
CCP
PPC

3



5
YCPZY
CYZZP
CCPPP
YCYZC
CPPZZ
"""

import sys

def checkRow(rowNum):
    count = 1
    max_count = 1
    iter_list = array[rowNum]
    start_value = iter_list[0]
    for i in range(1, n):
        if start_value == iter_list[i]:
            count += 1
            if count > max_count:
                max_count = count
        else :
            count = 1
        start_value = iter_list[i]
    return max_count

def checkCol(colNum):
    count = 1
    max_count = 1
    iter_list = [row[colNum] for row in array]
    start_value = iter_list[0]

    for i in range(1, n):
        if start_value == iter_list[i]:
            count += 1
            if count > max_count:
                max_count = count
        else :
            count = 1
        start_value = iter_list[i]
    return max_count

def swap(xs,ys):
    temp = array[xs[0]][ys[0]]
    array[xs[0]][ys[0]] = array[xs[1]][ys[1]]
    array[xs[1]][ys[1]] = temp

def checkPos(i,j):
    if i < 0 or i >= n or j < 0 or j >= n:
        return False
    else:
        return True

def printArray():
    for i in range(n):
        print(array[i])
        print()

def bombonni():
    global max_value
    for i in range(n):
        for j in range(n):
            for k in range(4):
                swap_x = i + dx[k]
                swap_y = j + dy[k]
                new_max = max(checkRow(i), checkCol(j))
                if max_value < new_max:
                    # print(i,j)
                    # print(new_max)
                    max_value = new_max

                if checkPos(swap_x,swap_y) :

                    ## 적합한 위치면,
                    ## swap, checkRow, checkCol, reswap
                    swap([i, swap_x],[j,swap_y])

                    new_max2 = max(checkRow(i), checkRow(swap_x), checkCol(j), checkCol(swap_y))

                    if max_value < new_max2 :
                        max_value = new_max2
                    swap([i, swap_x], [j, swap_y])






if __name__ == "__main__":

    n = int(sys.stdin.readline())

    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    array = list()

    max_value = 0

    for i in range(n):
        array.append(list(sys.stdin.readline().strip()))

    bombonni()
    print(max_value)