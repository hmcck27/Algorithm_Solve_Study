def solution(pos):

    row_index, column_index = pos[0], pos[1]

    row_index = ord(row_index)-97
    column_index = int(column_index)-1

    count = 0

    movement_list = [(-1,-2),(-2, -1),(-2, 1),(-1, 2),(1,2),(2,1),(2,-1),(1,-2)]
    # 8 movement check

    for i in movement_list:
        if 0 <= row_index + i[0] <= 7 and 0<=column_index + i[1] <= 7:
            count+=1

    return count



pos = "c2"
print(solution(pos))