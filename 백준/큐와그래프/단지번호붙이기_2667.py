"""
단지번호붙이기

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	128 MB	105917	44715	28204	40.181%
문제
<그림 1>과 같이 정사각형 모양의 지도가 있다. 1은 집이 있는 곳을, 0은 집이 없는 곳을 나타낸다. 철수는 이 지도를 가지고 연결된 집의 모임인 단지를 정의하고, 단지에 번호를 붙이려 한다. 여기서 연결되었다는 것은 어떤 집이 좌우, 혹은 아래위로 다른 집이 있는 경우를 말한다. 대각선상에 집이 있는 경우는 연결된 것이 아니다. <그림 2>는 <그림 1>을 단지별로 번호를 붙인 것이다. 지도를 입력하여 단지수를 출력하고, 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력하는 프로그램을 작성하시오.



입력
첫 번째 줄에는 지도의 크기 N(정사각형이므로 가로와 세로의 크기는 같으며 5≤N≤25)이 입력되고, 그 다음 N줄에는 각각 N개의 자료(0혹은 1)가 입력된다.

출력
첫 번째 줄에는 총 단지수를 출력하시오. 그리고 각 단지내 집의 수를 오름차순으로 정렬하여 한 줄에 하나씩 출력하시오.
"""

def bfs(i,j):

    need_visited = deque()
    need_visited.append((i,j))

    count = 0

    while need_visited:
        pop = need_visited.popleft()
        if not visited[pop[0]][pop[1]] and graph[pop[0]][pop[1]] == 1:
            visited[pop[0]][pop[1]] = True
            count += 1
            for x,y in zip(dx, dy):
                if pop[0] + x < 0 or pop[0] + x > n-1 or pop[1] + y < 0 or pop[1] + y > n-1:
                    continue
                if not visited[pop[0] + x][pop[1] + y] and graph[pop[0] + x][pop[1] + y] == 1:
                    need_visited.append((pop[0] + x, pop[1] + y))


    return count


if __name__ == "__main__":
    import sys
    from collections import deque

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    n = int(sys.stdin.readline().rstrip())

    graph = list()

    for i in range(n):
        graph.append(list(map(int, list(sys.stdin.readline().rstrip()))))

    visited = [[False for i in range(n)] for j in range(n)]

    ans = list()

    count = 0

    for i in range(n):
        for j in range(n):
            if not visited[i][j] and graph[i][j] == 1:
                ans.append(bfs(i,j))
                count += 1

    print(count)
    for i in sorted(ans):
        print(i)

