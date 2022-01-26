"""
쉬운 계단 수
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	256 MB	94553	29297	20977	29.038%
문제
45656이란 수를 보자.

이 수는 인접한 모든 자리의 차이가 1이다. 이런 수를 계단 수라고 한다.

N이 주어질 때, 길이가 N인 계단 수가 총 몇 개 있는지 구해보자. 0으로 시작하는 수는 계단수가 아니다.

입력
첫째 줄에 N이 주어진다. N은 1보다 크거나 같고, 100보다 작거나 같은 자연수이다.

출력
첫째 줄에 정답을 1,000,000,000으로 나눈 나머지를 출력한다.
"""
import sys
if __name__ == "__main__":

    n = int(sys.stdin.readline().rstrip())

    d = list()

    for i in range(101):
        d.append([0]*10)

    for i in range(1,10):
        d[1][i] = 1

    for i in range(2, 101):
        for j in range(0, 10):
            ans = 0
            if j-1 >= 0:
                ans += d[i-1][j-1]
            if j+1 <= 9:
                ans += d[i-1][j+1]
            d[i][j] = ans

    # print(d[2])

    print(sum(d[n])%1000000000)




