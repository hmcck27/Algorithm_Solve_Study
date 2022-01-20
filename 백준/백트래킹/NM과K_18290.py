"""

문제
크기가 N×M인 격자판의 각 칸에 정수가 하나씩 들어있다.

이 격자판에서 칸 K개를 선택할 것이고, 선택한 칸에 들어있는 수를 모두 더한 값의 최댓값을 구하려고 한다.
단, 선택한 두 칸이 인접하면 안된다. r행 c열에 있는 칸을 (r, c)라고 했을 때, (r-1, c), (r+1, c), (r, c-1), (r, c+1)에 있는 칸이 인접한 칸이다.

입력
첫째 줄에 N, M, K가 주어진다.
둘째 줄부터 N개의 줄에 격자판에 들어있는 수가 주어진다.

출력
선택한 칸에 들어있는 수를 모두 더한 값의 최댓값을 출력한다.

제한
1 ≤ N, M ≤ 10
1 ≤ K ≤ min(4, N×M)
격자판에 들어있는 수는 -10,000보다 크거나 같고, 10,000보다 작거나 같은 정수이다.
항상 K개의 칸을 선택할 수 있는 경우만 입력으로 주어진다.

2 2 2
5 4
4 5

10

2 2 2
1 2
3 4

5

5 5 3
1 9 8 -2 0
-1 9 8 -3 0
-5 1 9 -1 0
0 0 0 9 8
9 9 9 0 0

"""

import sys


def printArray(array):
    for i in array:
        print(i, end=" ")
    print()

def nmkComposition(left, array_x, array_y, x, y, sum_value):

    ## 처음 시작할때만 넣어주고 다른 재귀에서는 당연히 x,y는 포함안되게 해야한다.

    global max_value

    # print(left, array_x, array_y, x, y, sum_value)

    ## 탈출
    if left == 0:
        if max_value == None:
            max_value = sum_value
        elif max_value <= sum_value:
            max_value = sum_value
        return

    ## 반복
    for i in range(x, n):
        # 첫번째 줄 iterate
        if i == x:
            for j in range(y, m):
                # print(left, array_x, array_y, x, y, sum_value)
                if len(array_y) != 0:
                    if i == x and j == y:
                        continue
                if isPos(array_x,array_y,i,j):
                    # print(left, array_x, array_y, x, y, sum_value)
                    array_x.append(i)
                    array_y.append(j)
                    sum_value += nmList[i][j]

                    nmkComposition(left - 1, array_x, array_y, i, j, sum_value)

                    array_x.pop()
                    array_y.pop()
                    sum_value -= nmList[i][j]

        else :
            for j in range(m):
                if isPos(array_x,array_y,i,j):
                    # print(left, array_x, array_y, x, y, sum_value)
                    # print("asdf2")
                    ## 재귀 dfs 시작
                    array_x.append(i)
                    array_y.append(j)
                    sum_value += nmList[i][j]

                    nmkComposition(left-1, array_x, array_y, i, j, sum_value)

                    array_x.pop()
                    array_y.pop()
                    sum_value -= nmList[i][j]

def isPos(array_x,array_y, new_x, new_y):

    for x,y in zip(array_x,array_y):
        if abs(new_x - x) == 0 and abs(new_y - y) == 1:
            return False
        elif abs(new_x - x) == 1 and abs(new_y - y) == 0:
            return False

    return True

if __name__ == "__main__":

    n, m, k = map(int, sys.stdin.readline().strip().split())

    nmList = list()
    max_value = None

    dx = [0,0,-1,1,1,-1,1,-1]
    dy = [1,-1,0,0,1,-1,-1,1]

    dx = [1]
    dy = [1]

    for i in range(n):
        nmList.append(list(map(int, sys.stdin.readline().strip().split())))

    sum_value = 0
    count = 0

    nmkComposition(k, [], [], 0, 0, 0)
    nmkComposition(k, [], [], 0, 1, 0)

    print(max_value)