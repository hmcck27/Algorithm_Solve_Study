def solution(array, commands):
    answer = list()
    for i in commands:

        temp_list = array[i[0]-1:i[1]]

        temp_list.sort()

        answer.append(temp_list[i[2]-1])



    return answer








array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
print(solution(array, commands))