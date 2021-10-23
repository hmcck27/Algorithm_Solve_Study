'''



'''

N = 3
M = 3
board = [[3,1,2],[4,1,4],[2,2,2]]

# N = 2
# M = 4
# board = [[7,3,1,8],[3,3,3,4]]

def solution(N,M,board):


    result = 0
    for i in board:
        min_value = min(i)
        result = max(result, min_value)

    return result



print(solution(N,M,board))