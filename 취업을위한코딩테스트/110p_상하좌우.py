def solution(N, move_list):

    pos = [1,1]
    for i in move_list:
        if i == "R":
            if pos[1] + 1 > N:
                # cant move
                continue
            else :
                pos[1] += 1
        elif i == "L":
            if pos[1] - 1 < 1:
                continue
            else :
                pos[1] -= 1
        elif i == "U":
            if pos[0] - 1 < 1:
                continue
            else:
                pos[0] -= 1
        elif i == "D":
            if pos[0] + 1 > N:
                continue
            else:
                pos[0] += 1

    return pos



N = 5
move_list = ["R","R","R","U","D","D"]

print(solution(N, move_list))