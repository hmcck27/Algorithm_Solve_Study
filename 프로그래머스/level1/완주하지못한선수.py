def solution(participant, completion):

    par_dict = dict()
    com_dict = dict()

    for i in participant:
        if i in par_dict:
            par_dict[i] += 1
        else :
           par_dict[i] = 1

    for i in completion:
        if i in com_dict:
            com_dict[i] += 1
        else :
           com_dict[i] = 1


    # print(par_dict)
    # print(com_dict)

    for i in par_dict:
        if i in com_dict:
            par_dict[i] -= com_dict[i]

    for i in par_dict:
        if par_dict[i] >= 1:
            answer = i

    return answer


participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]

print(solution(participant, completion))

