"""
나이트의 이동 다국어

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	256 MB	33313	16379	12252	48.255%
문제
체스판 위에 한 나이트가 놓여져 있다. 나이트가 한 번에 이동할 수 있는 칸은 아래 그림에 나와있다. 나이트가 이동하려고 하는 칸이 주어진다. 나이트는 몇 번 움직이면 이 칸으로 이동할 수 있을까?



입력
입력의 첫째 줄에는 테스트 케이스의 개수가 주어진다.

각 테스트 케이스는 세 줄로 이루어져 있다. 첫째 줄에는 체스판의 한 변의 길이 l(4 ≤ l ≤ 300)이 주어진다. 체스판의 크기는 l × l이다. 체스판의 각 칸은 두 수의 쌍 {0, ..., l-1} × {0, ..., l-1}로 나타낼 수 있다. 둘째 줄과 셋째 줄에는 나이트가 현재 있는 칸, 나이트가 이동하려고 하는 칸이 주어진다.

출력
각 테스트 케이스마다 나이트가 최소 몇 번만에 이동할 수 있는지 출력한다.
"""

def knightMove(I, fromX, fromY, toX, toY):

    #bfs로 해야지 최소 이동 수를 구할 수 있다.

    visited = [[False for i in range(I)] for i in range(I)]
    visited_graph = [[0 for i in range(I)] for i in range(I)]
    visited_graph[fromX][fromY] = 0

    need_visited = deque()

    need_visited.append((fromX, fromY))

    while need_visited:

        pop = need_visited.popleft()

        if not visited[pop[0]][pop[1]]:

            visited[pop[0]][pop[1]] = True

            for i in range(8):
                if pop[0] + dx[i] < 0 or pop[0] + dx[i] > I-1 or pop[1] + dy[i] < 0  or pop[1] + dy[i] > I-1:
                    continue
                if not visited[pop[0]+dx[i]][pop[1]+dy[i]]:
                    need_visited.append((pop[0]+dx[i], pop[1]+dy[i]))
                    visited_graph[pop[0]+dx[i]][pop[1]+dy[i]] = visited_graph[pop[0]][pop[1]] + 1

    return visited_graph[toX][toY]


if __name__ == "__main__":

    import sys
    from collections import deque
    n = int(sys.stdin.readline().rstrip())

    dx = [-2,-1,1,2,1,2,-1,-2]
    dy = [-1,-2,2,1,-2,-1,2,1]

    fromXList = list()
    fromYList = list()
    toXList = list()
    toYList = list()
    IList = list()

    for i in range(n):

        I = int(sys.stdin.readline().rstrip())
        IList.append(I)
        fromX, fromY = map(int, sys.stdin.readline().rstrip().split())
        fromXList.append(fromX)
        fromYList.append(fromY)
        toX, toY = map(int, sys.stdin.readline().rstrip().split())
        toXList.append(toX)
        toYList.append(toY)

    for i in range(n):
        print(knightMove(IList[i], fromXList[i], fromYList[i], toXList[i] , toYList[i]))


