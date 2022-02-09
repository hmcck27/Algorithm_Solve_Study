"""
DFS와 BFS

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	128 MB	164973	58325	34371	34.711%
문제
그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

입력
첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.

출력
첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.
"""

def dfs(graph, v):

    need_visited = deque()
    visited = []

    need_visited.append(v)

    while need_visited:
        pop = need_visited.pop()
        if pop not in visited:
            visited.append(pop)
        for i in sorted(graph[pop], reverse=True):
            if i not in visited:
                need_visited.append(i)

    for i in visited:
        print(i, end=" ")
    print()


def bfs(graph, v):

    need_visited = deque()
    visited = []

    need_visited.append(v)

    while need_visited :
        pop = need_visited.popleft()
        if pop not in visited:
            visited.append(pop)
        for i in sorted(graph[pop]):
            if i not in visited:
                need_visited.append(i)

    for i in visited:
        print(i, end=" ")
    print()


if __name__ == "__main__":
    import sys
    from collections import deque

    n, m, v = map(int, sys.stdin.readline().rstrip().split())
    graph = [[] for i in range(n+1)]
    for i in range(m):
        a, b = map(int, sys.stdin.readline().rstrip().split())
        graph[a].append(b)
        graph[b].append(a)


    dfs(graph, v)
    bfs(graph, v)