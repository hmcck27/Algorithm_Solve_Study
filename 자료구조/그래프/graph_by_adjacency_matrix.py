# coding=utf-8
'''
    0번 노드는 1번 노드와 비용 7로 연결
    0번 노드는 2번 노드와 비용 5로 연결
    1번 노드는 0번 노드와 비용 7로 연결
    2번 노드는 0번 노드와 비용 5로 연결
'''

INF = 999999999

'''
sample_graph = [
    [0, 7, 5],
    [7, 0, INF],
    [5, INF, 0]
]
'''

N = 3
M = 3

graph = [[0 if j == i else INF for j in range(M)] for i in range(N)]

graph[0][1] = 7
graph[0][2] = 5
graph[1][0] = 7
graph[2][0] = 5

print(graph)
