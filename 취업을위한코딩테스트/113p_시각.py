def solution(N):

    count = 0
    for i in range(N+1):
        for j in range(1, 61):
            for k in range(1, 61):
                if "3" in str(k) or "3" in str(j) or "3" in str(i):
                    count += 1


    return count



N = 5
print(solution(N))