def solution(N,K):


    count = 0
    while True:
        print(N)

        if N == 1:
            break

        if N % K == 0:
            N /= K
            count += 1
        else :
            N -= 1
            count += 1


    return count




N = 25
K = 3
print(solution(N,K))