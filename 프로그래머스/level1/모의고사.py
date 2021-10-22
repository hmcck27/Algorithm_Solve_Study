def solution(answers):

    answer = []
    # 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
    # 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
    # 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...

    len1 = 5
    len2 = 8
    len3 = 10

    sample1 = [1,2,3,4,5]
    sample2 = [2,1,2,3,2,4,2,5]
    sample3 = [3,3,1,1,2,2,4,4,5,5]

    result1 = 0
    result2 = 0
    result3 = 0

    result_dict = dict()
    for i in range(1,4):
        result_dict[i] = 0

    for i in range(len(answers)):
        if answers[i] == sample1[(i)%(len1)]:
            result_dict[1] += 1
        if answers[i] == sample2[(i)%(len2)]:
            result_dict[2] += 1
        if answers[i] == sample3[(i)%(len3)]:
            result_dict[3] += 1


    # [1,2,3] -> [3]
    # [1,3,2] -> [2]
    # [3,3,1] -> [1,2]

    for i in result_dict:
        answer.append(result_dict[i])


    max_value = max(answer)
    result = list()

    for i in range(3):
        if max_value == answer[i]:
            result.append(i+1)

    return result


answer = [1,2,3,4,5]

print(solution(answer))