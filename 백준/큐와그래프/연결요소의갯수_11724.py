"""
연결 요소의 개수

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
3 초	512 MB	58563	27467	17980	43.816%
문제
방향 없는 그래프가 주어졌을 때, 연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 정점의 개수 N과 간선의 개수 M이 주어진다. (1 ≤ N ≤ 1,000, 0 ≤ M ≤ N×(N-1)/2) 둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v가 주어진다. (1 ≤ u, v ≤ N, u ≠ v) 같은 간선은 한 번만 주어진다.

출력
첫째 줄에 연결 요소의 개수를 출력한다.

6 5
1 2
2 5
5 1
3 4
4 6

2

"""

def dfs(graph, v):

    visited = []
    need_visisted = deque()
    need_visisted.append(v)

    while need_visisted:
        pop = need_visisted.pop()
        if pop not in visited:
            visited.append(pop)
            for i in graph[pop]:
                if i not in visited:
                    need_visisted.append(i)

    return visited

def bfs(graph, v, visited):


    need_visited = deque()
    need_visited.append(v)
    count = False
    while need_visited:
        pop = need_visited.popleft()
        if not visited[pop]:
            visited[pop] = True
            count = True
            for i in graph[pop]:
                if not visited[i]:

                    need_visited.append(i)

    return count

if __name__ == "__main__":
    import sys
    from collections import deque
    n , m = map(int, sys.stdin.readline().rstrip().split())
    graph = [[] for i in range(n+1)]
    for i in range(m):
        a,b = map(int, sys.stdin.readline().rstrip().split())
        graph[a].append(b)
        graph[b].append(a)

    count = 0
    visited = [False] * (n+1)
    for i in range(1, n + 1):
        if bfs(graph, i, visited):
            count += 1

    print(count)

