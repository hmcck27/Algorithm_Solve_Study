## dfs로 일단 서치
## 그리고 나서 예외 상황은 따로 서치

import sys

## input
n,m = map(int,sys.stdin.readline().split(" "))

graph = list()
for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().split(" "))))

## 전역변수 설정
bool_array = [[False for i in range(m)] for j in range(n)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def check_exshape():

    ## 예외적인 상황에서 체크한다.
    move_list = list()
    case1 = [[0,0],[0,1],[0,2],[-1,1]]
    case2 = [[0,0],[0,1],[-1,1],[1,1]]
    case3 = [[0, 0], [0, 1], [0, 2], [1, 1]]
    case4 = [[0, 0], [1, 0], [1, 1], [2, 0]]

    move_list.append(case1)
    move_list.append(case2)
    move_list.append(case3)
    move_list.append(case4)

    ## 총 4가지 상황이 있는데,

    result = 0

    for i in range(n):
        for j in range(m):

            ## 여기서 체크하기
            ## 총 4가지 경우가 있음

            for one_case in move_list:
                sum_ = 0
                for one_pos in one_case:
                    if i + one_pos[0] < 0 or i + one_pos[0] >= n or j + one_pos[1] < 0 or j + one_pos[1] >= m:
                        break
                    else :
                        sum_ += graph[i + one_pos[0]][j + one_pos[1]]
                        if sum_ > result :
                            result = sum_

    return result

ans = 0

def dfs(x,y,sum_value, length):

    global ans

    if length == 3:
        if ans < sum_value :
            ans = sum_value
        return

    for i in range(4):

        ## 새로운 진입점 세팅
        new_x = x + dx[i]
        new_y = y + dy[i]

        ## 이 진입점이 괜찮은 진입점인지 검사
        if new_x < 0 or new_x >= n or new_y < 0 or new_y >= m:
            continue

        ## 진입한 점인지 검사
        if bool_array[new_x][new_y] is not True:
            ## 괜찮은 진입점 이제 진입해야함
            bool_array[new_x][new_y] = True

            ## sum 더하기
            sum_value += graph[new_x][new_y]
            dfs(new_x, new_y, sum_value, length+1)

            ## 진입하고 빠져나옴
            bool_array[new_x][new_y] = False
            sum_value -= graph[new_x][new_y]



for i in range(n):
    for j in range(m):
        bool_array[i][j] = True
        dfs(i, j, graph[i][j], 0)
        bool_array[i][j] = False

ex = check_exshape()
# print(ex)
if ans < ex:
    ans = ex

print(ans)
