
def printArray(n,m,array):
    for i in range(n):
        for j in range(m):
            print(array[i][j], end=" ")
        print()

def rotate(n,m,array):
    newArray = [[0 for i in range(m)] for j in range(n)]

    for i in range(n):
        for j in range(m):
            # print(i,j)
            # 모서리 아닌 경우만 먼저
            if (i > j and i + j < n-1 and j < m//2):
                # 밑으로 이동
                # print("down")
                newArray[i+1][j] = array[i][j]
            elif ((m > n and j - i > m-n) or (n > m and i - j < n - m) or (m==n and j > i)) and i + j > m-1 and j >= m//2:
                # 위로 이동
                # print("up")
                newArray[i - 1][j] = array[i][j]
            elif (i < j and i + j < m-1 and i < n//2):
                # 왼쪽 이동
                # print("left")
                newArray[i][j-1] = array[i][j]
            elif ((m > n and j - i < m-n) or (n > m and i - j > n - m) or ( m==n and i > j)) and i + j > n-1 and i >= n//2 :
                # 오른쪽 이동
                # print("right")
                newArray[i][j+1] = array[i][j]

            else:
                # print("else")
                # 모서리 위치
                if i == j and i < n // 2 and j < m // 2:
                    # 아래 이동
                    # print("down")
                    newArray[i + 1][j] = array[i][j]
                elif i + j == n-1 and i >= n // 2 and j < m//2:
                    # print("right")
                    # 오른쪽 이동
                    newArray[i][j+1] = array[i][j]
                elif i + j == m - 1 and i < n // 2 and j >= m//2:
                    # 왼쪽 이동
                    # print("left")
                    newArray[i][j-1] = array[i][j]
                else:
                    # 위로 이동
                    # print("up")
                    newArray[i-1][j] = array[i][j]

    return newArray

if __name__ == "__main__":
    import sys
    n,m,r = map(int, sys.stdin.readline().rstrip().split())
    array = list()
    for i in range(n):
        array.append(list(map(int, sys.stdin.readline().rstrip().split())))

    for i in range(r):
        array = rotate(n,m,array)

    printArray(n,m,array)