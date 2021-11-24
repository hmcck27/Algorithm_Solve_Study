def solution(n):
    array = list()
    array.append(1)
    array.append(1)
    for i in range(2, n):
        array.append(array[i-1] + array[i-2])

    return array[n-1]

print(solution(n=10))