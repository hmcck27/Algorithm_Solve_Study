def solution(N, stages):
    answer = []
    leftNum = len(stages)

    fail_list = []
    for i in range(1,N+1):

        fail_num = 0
        for n in stages:
            if n == i:
                fail_num += 1

        if leftNum <= 0 :
            fail_list.append(0)
            continue
        else:
            # print(fail_num, leftNum)
            fail_list.append(float(fail_num)/leftNum)

        leftNum -= fail_num

    print(fail_list)

    count = 0
    fail_index_list = [m for m,value in enumerate(fail_list)]
    print(fail_index_list)

    for i in range(len(fail_list)):
        max_value = max(fail_list)
        max_index = fail_index_list[fail_list.index(max_value)]

        answer.append(max_index+1)

        fail_index_list.remove(max_index)
        fail_list.remove(max_value)


    return answer


N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]

N = 4
stages = [4,4,4,4,4]

# N = 7
# stages = [5,5,5,5,5,5]

print(solution(N, stages))