def solution(m, n, board):
    answer = 0

    newBoard = list()
    for i in range(n):
        temp = list()
        for j in range(m):
            temp.append(board[j][i])
        newBoard.append(temp)

    deleteSet = checkDeleteSet(m,n,newBoard)
    while deleteSet != set():

        for delete in deleteSet:
            newBoard[delete[0]][delete[1]] = ""
            newBoard[delete[0]+1][delete[1]] = ""
            newBoard[delete[0]][delete[1]+1] = ""
            newBoard[delete[0]+1][delete[1]+1] = ""

        for i in range(n):
            for j in range(m):
                if newBoard[i][j] == "":
                    newBoard[i].pop(j)
                    newBoard[i] = [""] + newBoard[i]

        deleteSet = checkDeleteSet(m,n,newBoard)

    for i in range(n):
        for j in range(m):
            if newBoard[i][j] == "":
                answer+=1

    return answer

def checkDeleteSet(m,n,board):
    deleteSet = set()
    for i in range(n-1):
        for j in range(m-1):
            if board[i][j] == board[i+1][j] == board[i][j+1] == board[i+1][j+1] != "":
                deleteSet.add((i,j))
    return deleteSet


if __name__ == "__main__":
    m = 4
    n = 5
    board = ["CCBDE", "AAADE", "AAABF", "CCBBF"]
    print(solution(m,n,board))