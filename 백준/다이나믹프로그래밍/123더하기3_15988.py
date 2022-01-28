"""
1, 2, 3 더하기 3

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초 (추가 시간 없음)	512 MB	16116	5886	4363	34.996%
문제
정수 4를 1, 2, 3의 합으로 나타내는 방법은 총 7가지가 있다. 합을 나타낼 때는 수를 1개 이상 사용해야 한다.

1+1+1+1
1+1+2
1+2+1
2+1+1
2+2
1+3
3+1
정수 n이 주어졌을 때, n을 1, 2, 3의 합으로 나타내는 방법의 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고, 정수 n이 주어진다. n은 양수이며 1,000,000보다 작거나 같다.

출력
각 테스트 케이스마다, n을 1, 2, 3의 합으로 나타내는 방법의 수를 1,000,000,009로 나눈 나머지를 출력한다.
"""

if __name__ == "__main__":

    import sys

    n = int(sys.stdin.readline().rstrip())
    nList = list()

    for i in range(n):
        nList.append(int(sys.stdin.readline().rstrip()))

    max_value = max(nList)

    d = [[0 for i in range(4)] for j in range(max_value + 1)]

    d[1][1] = 1
    d[2][1] = d[2][2] = 1
    d[3][1] = 2
    d[3][2] = d[3][3] = 1

    for i in range(4, max_value + 1):
        for j in range(1, 4):
            d[i][j] = (d[i - j][1] + d[i - j][2] + d[i - j][3]) % 1000000009

    for i in nList:
        print(sum(d[i]) % 1000000009)




