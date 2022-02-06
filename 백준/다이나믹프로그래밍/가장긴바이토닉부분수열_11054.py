"""
가장 긴 바이토닉 부분 수열

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	256 MB	30858	15703	12290	50.947%
문제
수열 S가 어떤 수 Sk를 기준으로 S1 < S2 < ... Sk-1 < Sk > Sk+1 > ... SN-1 > SN을 만족한다면, 그 수열을 바이토닉 수열이라고 한다.

예를 들어, {10, 20, 30, 25, 20}과 {10, 20, 30, 40}, {50, 40, 25, 10} 은 바이토닉 수열이지만,  {1, 2, 3, 2, 1, 2, 3, 2, 1}과 {10, 20, 30, 40, 20, 30} 은 바이토닉 수열이 아니다.

수열 A가 주어졌을 때, 그 수열의 부분 수열 중 바이토닉 수열이면서 가장 긴 수열의 길이를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 수열 A의 크기 N이 주어지고, 둘째 줄에는 수열 A를 이루고 있는 Ai가 주어진다. (1 ≤ N ≤ 1,000, 1 ≤ Ai ≤ 1,000)

출력
첫째 줄에 수열 A의 부분 수열 중에서 가장 긴 바이토닉 수열의 길이를 출력한다.

10
1 5 2 1 4 3 4 5 2 1

7
"""

if __name__ == "__main__":
    import sys
    n = int(sys.stdin.readline().rstrip())
    nList = list(map(int, sys.stdin.readline().rstrip().split()))
    nList = [0] + nList
    max_value = max(nList)
    # if max_value % 2 == 0:
    #     max_value += 1
    d = [0] * (max_value * 2)
    for i in range(1, n+1):

        if nList[i] == max_value:
            d[nList[i]] = max(d[:nList[i]]) + 1
        else :
            d[nList[i]] = max(d[:nList[i]]) + 1
            d[2*max_value-nList[i]] = max(d[nList[i]+1 : 2*max_value-nList[i]]) + 1



    print(max(d))