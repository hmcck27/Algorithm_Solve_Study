def solution(n):
    answer = 0

    result = []

    while True:
        if n/3 < 3:
            result.append(n%3)
            if n//3 != 0:
                result.append(n//3)
            break

        result.append(n%3)
        n = n//3

    while result[0] == 0:
        result.pop(0)

    for i in range(len(result)):
        answer += result[i] * (3**(len(result)-1-i))


    return answer


n = 1
print(solution(n))