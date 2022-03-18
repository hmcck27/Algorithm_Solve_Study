def bfs(miro, col, row, visited, queue):


    while len(queue) != 0 :

        pop_value = queue.popleft()

        new_row = pop_value[0]
        new_col = pop_value[1]

        # 상하좌우 큐 넣기 -> 무조건 큐에는 벽이 없는곳을 먼저 넣어야 한다.

        for i,j in zip(dx, dy):

            # 미로 범위 체크
            if new_col + i < col and new_row + j < row and new_row + j >= 0 and new_col + i >= 0:

                # 방문하지 않은 곳.
                if not visited[new_row + j][new_col + i]:
                    temp = [new_row + j, new_col + i]
                    # 벽이 없는 곳 먼저.
                    if miro[new_row + j][new_col + i] == 0:
                        visited2[new_row + j][new_col + i] = visited2[new_row][new_col]
                        visited[new_row+j][new_col+i] = True
                        queue.appendleft(temp)
                    else:
                        # 벽 있는 경우는 나중에 넣어야한다.
                        if (visited2[new_row+j][new_col + i] != 0 and visited2[new_row][new_col] + 1 > visited2[new_row + j][new_col + i]):
                            visited2[new_row + j][new_col + i] = visited2[new_row][new_col]
                        else:
                            visited2[new_row + j][new_col + i] = visited2[new_row][new_col] + 1
                        visited[new_row + j][new_col + i] = True
                        queue.append(temp)

    return visited2[row-1][col-1]



if __name__ == "__main__":

    from collections import deque

    import sys

    col_num, row_num = map(int, sys.stdin.readline().split())

    miro = []

    for i in range(row_num):
        temp = sys.stdin.readline().rstrip()
        list_ = [i for i in temp]
        miro.append(list(map(int, list_)))

    visited = [[False for i in range(col_num)] for i in range(row_num)]
    visited2 = [[0 for i in range(col_num)] for i in range(row_num)]

    # 상하가 y좌표, 좌우가 x좌표

    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    queue = deque()
    queue.append([0,0])

    visited[0][0] = 1

    print(bfs(miro, col_num, row_num, visited, queue))