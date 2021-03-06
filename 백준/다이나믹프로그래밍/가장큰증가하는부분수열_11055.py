"""
문제
수열 A가 주어졌을 때, 그 수열의 증가 부분 수열 중에서 합이 가장 큰 것을 구하는 프로그램을 작성하시오.

예를 들어, 수열 A = {1, 100, 2, 50, 60, 3, 5, 6, 7, 8} 인 경우에 합이 가장 큰 증가 부분 수열은 A = {1, 100, 2, 50, 60, 3, 5, 6, 7, 8} 이고, 합은 113이다.

입력
첫째 줄에 수열 A의 크기 N (1 ≤ N ≤ 1,000)이 주어진다.

둘째 줄에는 수열 A를 이루고 있는 Ai가 주어진다. (1 ≤ Ai ≤ 1,000)

출력
첫째 줄에 수열 A의 합이 가장 큰 증가 부분 수열의 합을 출력한다.

10
2 11 3 14 1 200 100 5 101 13
[0, 2, 13, 5, 27, 6, 227, 127, 232, 228, 26]
[0, 2, 13, 3, 14, 1, 200, 114, 5, 101, 26]

5
10 90 20 80 100
[0, 10, 100, 30, 110, 200]
"""

if __name__ == "__main__":

    import sys

    n = int(sys.stdin.readline().rstrip())
    nList = list(map(int, sys.stdin.readline().rstrip().split()))
    nList = [0] + nList

    d = [0] * (1001)
    d[nList[1]] = nList[1]

    for i in range(2, n+1):
        d[nList[i]] = max(d[:nList[i]]) + nList[i]


    print(max(d))