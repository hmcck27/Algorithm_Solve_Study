"""
문제
정수 4를 1, 2, 3의 합으로 나타내는 방법은 총 3가지가 있다. 합을 나타낼 때는 수를 1개 이상 사용해야 한다. 단, 같은 수를 두 번 이상 연속해서 사용하면 안 된다.

1+2+1
1+3
3+1
정수 n이 주어졌을 때, n을 1, 2, 3의 합으로 나타내는 방법의 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고, 정수 n이 주어진다. n은 양수이며 100,000보다 작거나 같다.

출력
각 테스트 케이스마다, n을 1, 2, 3의 합으로 나타내는 방법의 수를 1,000,000,009로 나눈 나머지를 출력한다.
"""

import sys

def dpMake(n):
    for i in range(3, n+1):

        if i - 4 < 0:
            d[i] = d[i-1] + d[i-2] + 1
        elif i - 6 < 0:
            d[i] = (d[i-1] - d[i-2]) + (d[i-2] - d[i-4])
        else:
            d[i] = (d[i-1] - d[i-2]) +  (d[i-2] - d[i-4]) + (d[i-3] - d[i-6])


if __name__ == "__main__":
    n = int(sys.stdin.readline().rstrip())

    nList = list()

    d = [0]*100001
    d[0] = 0
    d[1] = 1
    d[2] = 1
    d[3] = 3
    d[4] = 3

    for i in range(n):
        nList.append(int(sys.stdin.readline().rstrip()))

    dpMake(max(nList))

    for i in nList:
        print(d[i])

    print(d[:11])
