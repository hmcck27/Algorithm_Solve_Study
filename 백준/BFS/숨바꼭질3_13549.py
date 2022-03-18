def bfs(n,m,queue, visited):
    min_value = 100001
    while len(queue) != 0:

        pop_value = queue.popleft()

        if pop_value[0] == m and min_value > pop_value[1]:
            min_value = pop_value[1]
            continue


        # 2 * 이동
        if pop_value[0] * 2 <= 100000 and not visited[pop_value[0]*2] and pop_value[1] <= min_value:
            temp = [pop_value[0] * 2, pop_value[1]]
            queue.append(temp)
            visited[pop_value[0] * 2] = True
        # -1이동
        if pop_value[0] - 1 >= 0 and not visited[pop_value[0]-1] and pop_value[1]+1 < min_value:
            temp = [pop_value[0] - 1, pop_value[1]+1]
            queue.append(temp)
            visited[pop_value[0]-1] = True
        # +1 이동
        if pop_value[0] + 1 <= 100000 and not visited[pop_value[0]+1] and pop_value[1]+1 < min_value:
            temp = [pop_value[0] + 1, pop_value[1] + 1]
            queue.append(temp)
            visited[pop_value[0] + 1] = True



    return min_value

if __name__ == "__main__":
    from collections import deque
    import sys
    n, m = map(int, sys.stdin.readline().rstrip().split())
    visited = [False for i in range(100001)]
    queue = deque()
    visited[n] = True
    queue.append([n,0])
    print(bfs(n,m,queue,visited))
