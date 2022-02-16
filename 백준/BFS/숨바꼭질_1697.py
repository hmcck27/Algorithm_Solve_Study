"""
숨바꼭질 다국어

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	128 MB	138140	39172	24503	25.036%
문제
수빈이는 동생과 숨바꼭질을 하고 있다. 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다. 수빈이는 걷거나 순간이동을 할 수 있다. 만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다. 순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동하게 된다.

수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램을 작성하시오.

입력
첫 번째 줄에 수빈이가 있는 위치 N과 동생이 있는 위치 K가 주어진다. N과 K는 정수이다.

출력
수빈이가 동생을 찾는 가장 빠른 시간을 출력한다.
"""

if __name__ == "__main__":

    import sys
    from collections import deque

    n, k = map(int, sys.stdin.readline().rstrip().split())

    visited = [False for i in range(100001)]
    visited_list = [0 for i in range(100001)]

    need_visited = deque()
    need_visited.append(n)
    ans = 0
    while need_visited:
        pop = need_visited.popleft()
        if not visited[pop]:
            visited[pop] = True
            if pop == k:
                break
            if pop + 1 < 100001 and visited_list[pop+1] == 0:
                visited_list[pop+1] = visited_list[pop] + 1
                need_visited.append(pop+1)
            if pop * 2 < 100001 and visited_list[pop*2] == 0:
                visited_list[pop*2] = visited_list[pop] + 1
                need_visited.append(pop*2)
            if pop - 1 >= 0 and visited_list[pop-1] == 0:
                visited_list[pop-1] = visited_list[pop] + 1
                need_visited.append(pop-1)


    print(visited_list[k])
