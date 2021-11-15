import sys
n = int(sys.stdin.readline().rstrip())
board = [0] * 15

def queen_overlap(low):
    # queen때문에 다음 low에 둘 수 없으면 false 반환
    for i in range(0, low):
        if board[i] == board[low] or abs(i-low) == abs(board[i]-board[low]):
            return True
    return False

def n_queen(count_queen,n):
    global count
    if count_queen == n:
        count += 1
    else:
        for i in range(n):
            board[count_queen] = i
            if not queen_overlap(count_queen):
                n_queen(count_queen+1, n)


count = 0
n_queen(0, n)
print(count)