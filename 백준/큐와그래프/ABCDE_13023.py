"""
ABCDE

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	512 MB	17057	5214	3473	29.209%
문제
BOJ 알고리즘 캠프에는 총 N명이 참가하고 있다. 사람들은 0번부터 N-1번으로 번호가 매겨져 있고, 일부 사람들은 친구이다.

오늘은 다음과 같은 친구 관계를 가진 사람 A, B, C, D, E가 존재하는지 구해보려고 한다.

A는 B와 친구다.
B는 C와 친구다.
C는 D와 친구다.
D는 E와 친구다.
위와 같은 친구 관계가 존재하는지 안하는지 구하는 프로그램을 작성하시오.

입력
첫째 줄에 사람의 수 N (5 ≤ N ≤ 2000)과 친구 관계의 수 M (1 ≤ M ≤ 2000)이 주어진다.

둘째 줄부터 M개의 줄에는 정수 a와 b가 주어지며, a와 b가 친구라는 뜻이다. (0 ≤ a, b ≤ N-1, a ≠ b) 같은 친구 관계가 두 번 이상 주어지는 경우는 없다.

출력
문제의 조건에 맞는 A, B, C, D, E가 존재하면 1을 없으면 0을 출력한다.

5 4
0 1
1 2
2 3
3 4

1

5 5
0 1
1 2
2 3
3 0
1 4
"""

def dfs(v, visited, depth):

    global ans

    if depth == 5:
        ans = True
        return

    for i in graph[v]:
        if i not in visited:
            visited.append(i)
            dfs(i, visited, depth+1)
            visited.pop()

if __name__ == "__main__":

    import sys

    n, m = list(map(int, sys.stdin.readline().rstrip().split()))
    graph = [[] for i in range(n)]

    for i in range(m):
        a,b = map(int, sys.stdin.readline().rstrip().split())
        graph[a].append(b)
        graph[b].append(a)

    ans = False

    for i in range(n):
        dfs(i, visited=[i], depth=1)
        if ans == True:
            break

    if ans:
        print(1)
    else:
        print(0)

