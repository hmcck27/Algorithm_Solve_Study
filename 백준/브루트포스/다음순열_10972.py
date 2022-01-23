"""
1부터 N까지의 수로 이루어진 순열이 있다.
이때, 사전순으로 다음에 오는 순열을 구하는 프로그램을 작성하시오.

사전 순으로 가장 앞서는 순열은 오름차순으로 이루어진 순열이고,
가장 마지막에 오는 순열은 내림차순으로 이루어진 순열이다.

N = 3인 경우에 사전순으로 순열을 나열하면 다음과 같다.

1, 2, 3
1, 3, 2
2, 1, 3
2, 3, 1
3, 1, 2
3, 2, 1
입력
첫째 줄에 N(1 ≤ N ≤ 10,000)이 주어진다. 둘째 줄에 순열이 주어진다.

출력
첫째 줄에 입력으로 주어진 순열의 다음에 오는 순열을 출력한다. 만약, 사전순으로 마지막에 오는 순열인 경우에는 -1을 출력한다.

4
1 2 3 4

순열의 원리를 파악해서 오름차순으로 가는게 핵심
여기서 재귀를 사용한 백트래킹을 사용하면 안된다.

"""

import sys

def comp():

    global nList

    for i in range(len(nList)-1, 0, -1):
        for j in range(i-1, -1, -1):
            if nList[i] > nList[j]:
                temp = nList[i]
                nList[i] = nList[j]
                nList[j] = temp
                return
            else:
                continue

    nList = [-1]

if __name__ == "__main__":
    n = int(sys.stdin.readline().rstrip())
    nList = list(map(int, sys.stdin.readline().rstrip().split()))
    comp()
    for i in nList:
        print(i, end=" ")
