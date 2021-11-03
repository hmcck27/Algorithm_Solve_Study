import sys

'''
    이런 문제를 파라메트릭 서치라고 부른다 !!
    
    
'''




def solution(N, M, array):

    result = 0
    max_value = max(array)

    start = 0
    end = max_value

    while start <= end:

        count = 0
        middle = (start + end) // 2
        for i in array:
            if i > middle:
                count += i-middle
            else :
                continue

        if count >= M:
            result = middle
            start = middle+1
        else :
            end = middle-1

    return result




N, M = map(int, input().split())
array = [int(i) for i in sys.stdin.readline().rstrip().split()]

print(solution(N,M,array))