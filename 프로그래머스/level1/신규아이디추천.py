def solution(new_id):

    answer = ''
    id_list = list(new_id)
    for i in range(len(id_list)):
        if 90 >= ord(id_list[i]) and ord(id_list[i]) >= 65:
            id_list[i] = chr(ord(id_list[i]) + 32)

    print("1")
    print(id_list)

    for i in range(len(id_list)):
        if (id_list[i] != '_') and (id_list[i] != '-') and (id_list[i] != '.') and not \
                ('0' <= id_list[i] <= '9') and not (
                122 >= ord(id_list[i]) >= 97):
            id_list[i] = ''

    id_list = list("".join(id_list))
    print("2")
    print(id_list)

    for i in range(len(id_list) - 1):
        if id_list[i] == '.':
            for j in range(i + 1, len(id_list)):
                if id_list[j] == '.':
                    id_list[j] = ''
                else:
                    break

    id_list = list("".join(id_list))
    print("3")
    print(id_list)

    if id_list[0] == '.':
        id_list[0] = ''
    if id_list[len(id_list) - 1] == '.':
        id_list[len(id_list) - 1] = ''

    id_list = list("".join(id_list))
    print("4")
    print(id_list)

    if not id_list:
        id_list = ["a"]

    print("5")
    print(id_list)

    if len(id_list) >= 16:
        id_list = id_list[:15]
        if id_list[len(id_list)-1] == '.':
            id_list[len(id_list)-1] = ""


    id_list = list("".join(id_list))
    print("6")
    print(id_list)


    if len(id_list) <= 2:
        end_char = id_list[len(id_list) - 1]
        while len(id_list) < 3:
            id_list.append(end_char)

    print("7")
    print(id_list)
    answer = "".join(id_list)

    return answer

new_id = "123_.def"

print(solution(new_id))
