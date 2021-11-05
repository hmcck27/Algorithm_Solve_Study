import sys

n = int(sys.stdin.readline().rstrip())

chess_board = [[0 for i in range(n)] for j in range(n)]

def queen_overlap(n, board, next_pos):
    # queen때문에 특정 자리에 둘 수 없으면 false 반환
    if board[next_pos[0]][next_pos[1]] == 1:
        return True
    else:
        return False

def fill_board(board, next_pos):

    # 세로선 가로선 처리
    fill_index_list = list()

    for i in range(n):
        for j in range(n):
            if board[i][j] == 0:
                if i == next_pos[0]:
                    # print('fir')
                    board[i][j] = 1
                    fill_index_list.append((i,j))
                elif j == next_pos[1]:
                    # print('sec')
                    board[i][j] = 1
                    fill_index_list.append((i, j))
                elif abs(next_pos[0] - i) == abs(next_pos[1] - j):
                    # print("thi")
                    board[i][j] = 1
                    fill_index_list.append((i, j))
    # printboard(board)
    return fill_index_list

def empty_board(board, fill_index_list):
    # print("empty board")
    # print(fill_index_list)
    for i in fill_index_list:
        board[i[0]][i[1]] = 0
    # printboard(board)


def printboard(board):
    for i in range(n):
        print(board[i])

def n_queen(left_queen, count, board):


    # print("-------------")
    # print("left_queen : ",left_queen)
    # printboard(board)
    result = 0

    if left_queen == 0:
        # print("search over !")
        return 1

    for i in range(n):
        for j in range(n):
            next_pos = (i,j)
            # print("next_pos", next_pos)
            # printboard(board)
            if queen_overlap(n, board, next_pos):
                # print('queen overlap')
                continue
            else :
                ## 보드 처리
                fill_index_list = fill_board(board, next_pos)

                # printboard(board)
                ## 재귀로 다시 돌리기

                result += n_queen(left_queen-1, count, board)
                empty_board(board, fill_index_list)

    return result

print(n_queen(n, 0, board=chess_board))