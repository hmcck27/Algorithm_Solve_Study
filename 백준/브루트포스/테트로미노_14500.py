import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

array = list()

for _ in range(n):

    array.append(list(map(int, sys.stdin.readline().rstrip().split())))

move_list = list()


## 세로 혹은 가로로 쭉 길게 4칸 이어진거
move_list1 = [(0,0), (0,1), (0,2), (0,3)]
move_list2 = [(0,0),(1,0),(2,0),(3,0)]

## 정사각형 모양
move_list3 = [(0,0),(1,0),(0,1),(1,1)]

## ㄱ 자 모양 1
move_list4 = [(0,0), (1,0), (2,0), (2,1)]
move_list5 = [(0,0), (0,1), (0,2), (-1,2)]
move_list6 = [(0,0), (-1,0), (-2,0), (-2,-1)]
move_list7 = [(0,0), (0,-1), (0,-2), (-1,-2)]

## ㄱ 자 모양 2
move_list15 = [(0,0),(0,1),(-1,1),(-2,1)]
move_list16 = [(0,0),(0,1),(0,2),(-1,2)]
move_list17 = [(0,0),(0,1),(1,0),(2,0)]
move_list18 = [(0,0),(-1,0),(0,1),(0,2)]

## 벌레 모양 1
move_list8 = [(0,0), (1,0), (1,1), (2,1)]
move_list9 = [(0,0), (0,1), (-1,1), (-1,2)]

## 벌레 모양 2
move_list13 = [(0,0), (1,0), (1,-1), (2,-1)]
move_list14 = [(0,0), (0,1), (1,1), (1,2)]


move_list5 = [(0,0), (0,1), (0,2), (1,1)]

move_list6 = [(0,1), (1,1), (2,1), (2,0)]

move_list7 = [(0,1), (1,1), (1,0), (2,0)]

"""
    1. 일단은 테트로미노를 총 7개의 형태로 정의하구
    2. 한칸을 기준으로 테트리미노의 좌표를 표시한다
    3. 그리고 표를 회전하거나 대칭시켜서 확인한다
"""

for i in range(0, n):
    for j in range(0, m) :


def transformArray():
    N = len(array)
    ret = array
    ret90 = [[0] * N for _ in range(N)]
    ret180 = [[0] * N for _ in range(N)]
    ret270 = [[0] * N for _ in range(N)]


    for r in range(N):
        for c in range(N):
            ret90[c][N - 1 - r] = m[r][c]
            ret180[][]


    return ret


for array in transformArray(array):
    for i in range(len(array)):
        for j in range(len(array[i])):
            for a, b in move_list1:
                sum_ = 0
                if not i+a <= n and 0<=i+a and 0<=j+b and j+b<=m:
                    break
                else:
                    sum_ += array[i+a][j+b]
