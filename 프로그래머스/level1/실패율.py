
def solution(N, stages):
    answer = []
    numOfPeople = len(stages)
    for i in range(1, N+1):
        fail_num = 0
        for j in range(len(stages)):
            if stages[j] == i:
                fail_num += 1

        print(i)
        print(fail_num, numOfPeople)

        if numOfPeople == 0:
            for j in range(i+1,N+1):
                answer.append(0)
            break
        elif fail_num == numOfPeople:
            answer.append(1)
            for j in range(len(answer), N):
                answer.append(0)
            break
        else :
            answer.append(float(fail_num)/numOfPeople)
            numOfPeople -= fail_num



    result_list = list()

    chk_list = [False for i in range(len(stages))]

    temp_list = answer[:]

    print(answer)

    for j in range(len(answer)):
        max_value = max(temp_list)
        for i, value in enumerate(answer):
            if value == max_value and chk_list[i] is not True:
                result_list.append(i+1)
                chk_list[i] = True
                break

        temp_list.remove(value)

    return result_list


stages = [4,4,4,4,4]
N = 5

print(solution(N, stages))