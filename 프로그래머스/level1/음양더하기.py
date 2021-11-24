def solution(absolutes, signs):
    answer = 0

    for i, j in zip(absolutes, signs):
        answer += (i if j == True else i*(-1))

    return answer



absolutes = [1,2,3]
signs = [False,False,True]

print(solution(absolutes, signs))