def solution(N, M, pos, board):
    answer = 1

    present_pos = pos[:2]
    present_dir = pos[2]

    for i in range(N):
        if i == 0: chk_board = list()

        chk_board.append(list())
        for j in range(M):
            chk_board[i].append(0)

    print(chk_board)
    chk_board[present_pos[0]][present_pos[1]] = 1
    cant_go_count = 0
    while True:

        move_flag = False


        if present_dir == 0:
            present_dir = 3
            print("try to go", present_pos[0], present_pos[1] - 1)
            if board[present_pos[0]][present_pos[1] - 1] == 0 and chk_board[present_pos[0]][present_pos[1] - 1] == 0:
                chk_board[present_pos[0]][present_pos[1] - 1] = 1
                present_pos = [present_pos[0], present_pos[1] - 1]
                move_flag = True
                answer += 1
                cant_go_count = 0
            else:
                print("cant go")
                cant_go_count +=1
        elif present_dir == 1:
            present_dir = 0
            print("try to go", present_pos[0] - 1,present_pos[1])
            if board[present_pos[0] - 1][present_pos[1]] == 0 and chk_board[present_pos[0] - 1][present_pos[1]] == 0:
                chk_board[present_pos[0] - 1][present_pos[1]] = 1
                present_pos = [present_pos[0] - 1, present_pos[1]]
                move_flag = True
                answer += 1
                cant_go_count = 0
            else:
                print("cant go")
                cant_go_count += 1
        elif present_dir == 2:
            present_dir = 1
            print("tyro to go", present_pos[0],present_pos[1] + 1)
            if board[present_pos[0]][present_pos[1] + 1] == 0 and chk_board[present_pos[0]][present_pos[1] + 1] == 0:
                chk_board[present_pos[0]][present_pos[1] + 1] = 1
                present_pos = [present_pos[0], present_pos[1] + 1]
                move_flag = True
                answer += 1
                cant_go_count = 0
            else :
                print("cant go")
                cant_go_count += 1
        else:
            present_dir = 2
            print("try to go", present_pos[0] + 1,present_pos[1])
            if board[present_pos[0] + 1][present_pos[1]] == 0 and chk_board[present_pos[0] + 1][present_pos[1]] == 0:
                chk_board[present_pos[0] + 1][present_pos[1]] = 1
                present_pos = [present_pos[0] + 1, present_pos[1]]
                move_flag = True
                answer += 1
                cant_go_count = 0
            else:
                print("cant go")
                cant_go_count += 1

        if cant_go_count == 4:
            print(chk_board)
            return answer


        if not move_flag:
            print(cant_go_count)
            print(present_pos)
            continue





N = 4
M = 4
pos = [1, 1, 0]
board = [[1, 1, 1, 1], [1, 0, 0, 1], [1, 1, 0, 1], [1, 1, 1, 1]]

print(solution(N, M, pos, board))
