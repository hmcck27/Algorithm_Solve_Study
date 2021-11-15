
def noAlpha(number_dict, s):

    for i in number_dict:
        if number_dict[i] in s:
            return False, i

    return True, True



def solution(s):
    answer = 0

    number_dict = {}

    number_dict[0] = "zero"
    number_dict[1] = "one"
    number_dict[2] = "two"
    number_dict[3] = "three"
    number_dict[4] = "four"
    number_dict[5] = "five"
    number_dict[6] = "six"
    number_dict[7] = "seven"
    number_dict[8] = "eight"
    number_dict[9] = "nine"

    for i in number_dict:
        if number_dict[i] in s:
            s = s.replace(number_dict[i], str(i))


    answer = int(s)



    return answer

s = "one4seveneight"

print(solution(s))