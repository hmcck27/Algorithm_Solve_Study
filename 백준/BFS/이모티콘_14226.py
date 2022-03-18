import sys

def bfs(visited, queue):
    min_value = 2000
    while len(queue) != 0:

        pop_value = queue.popleft()
        # 탈출 조건

        if pop_value[0] == n and min_value > pop_value[2]:
            min_value = pop_value[2]
            continue



        # 복사
        if not visited[pop_value[0]][pop_value[0]] and pop_value[2] + 1 < min_value:
            temp = [pop_value[0], pop_value[0], pop_value[2]+1]
            queue.append(temp)
            visited[pop_value[0]][pop_value[0]] = True
        # 븥이기
        if pop_value[0] + pop_value[1] <= n and pop_value[0] + pop_value[1] >= 0:
            if not visited[pop_value[0]+pop_value[1]][pop_value[1]] and pop_value[2] + 1 < min_value:
                temp = [pop_value[0]+pop_value[1], pop_value[1], pop_value[2] + 1]
                visited[pop_value[0]+pop_value[1]][pop_value[1]] = True
                queue.append(temp)
        # 삭제
        if pop_value[0] - 1 >= 0:
            if not visited[pop_value[0]-1][pop_value[1]] and pop_value[2] + 1 < min_value:
                temp = [pop_value[0]-1, pop_value[1], pop_value[2] + 1]
                visited[pop_value[0]-1][pop_value[1]] = True
                queue.append(temp)

    return min_value

if __name__ == "__main__":
    from collections import deque
    n = int(sys.stdin.readline().rstrip())
    operationQueue = deque()
    visited = [[False for j in range(n+1)] for i in range(n+1)]
    operationQueue.append([1,0,0])
    visited[1][0] = True

    print(bfs(visited, operationQueue))