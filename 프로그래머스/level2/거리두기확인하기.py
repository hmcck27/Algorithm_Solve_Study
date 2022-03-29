from collections import deque

flag = True

def solution(places):
    answer = []
    global flag
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]

    for place in places:
        # dfs로 구현하면서
        # 사람 앉은 곳이 나오면 flag를 갱신하고 기존
        # print(places.index(place))
        flag = True

        visitList = []
        for i in range(5):
            for j in range(5):
                if place[i][j] == "P":
                    visitList.append([i,j])

        visited = [[False for _ in range(5)] for __ in range(5)]

        for i in range(5):
            for j in range(5):
                if place[i][j] == "X":
                    visited[i][j] = True

        for visit in visitList:
            if not visited[visit[0]][visit[1]] and flag == True:
                bfs(place, visit, visited, dx, dy)

        if flag == True:
            answer.append(1)
        else:
            answer.append(0)

    return answer


def bfs(place, toVisit, visited, dx, dy):

    needVisited = deque()
    needVisited.appendleft(toVisit+[0])
    global flag
    isMain = True
    while len(needVisited) != 0:
        toVisit = needVisited.pop()
        visited[toVisit[0]][toVisit[1]] = True
        getFromPerson = toVisit[2]
        # print(toVisit[0:2], getFromPerson)
        if place[toVisit[0]][toVisit[1]] == "P" :
            if getFromPerson < 2 and not isMain:
                # 사람을 만났고,
                # 거리거 2 이하.
                flag = False
                print("asdf")
                return
            else:
                getFromPerson = 0

        else:
            getFromPerson += 1

        isMain = False
        # print(toVisit[0:2], getFromPerson)

        for x, y in zip(dx, dy):
            if x + toVisit[0] <= 4 and x + toVisit[0] >= 0 and y + toVisit[1] <= 4 and y + toVisit[1] >= 0:
                if not visited[x + toVisit[0]][y + toVisit[1]] and not (x + toVisit[0], y + toVisit[1]) in needVisited:
                    # 움직일 수 있는 좌표면

                    # 큐에 넣기
                    needVisited.appendleft([x + toVisit[0], y + toVisit[1], getFromPerson])


if __name__ == "__main__":
    places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
    print(solution(places))