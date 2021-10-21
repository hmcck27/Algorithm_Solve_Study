def findPosition(n):
    whole_list = [
        [1,2,3],[4,5,6],[7,8,9],["*", 0, "#"]
    ]
    for i in range(len(whole_list)):
        for j in range(len(whole_list[0])):
            if whole_list[i][j] == n:
                return i,j

def calculateDistance(pos1, pos2):
    return abs(pos1[0]-pos2[0]) + abs(pos1[1]-pos2[1])


def solution(numbers, hand):
    answer = ''

    left_list = [1, 4, 7]
    right_list = [3, 6, 9]

    answer = list()

    right_hand_pos = (3,2)
    left_hand_pos = (3,0)
    result = 0

    for i in numbers :

        dist_pos = findPosition(i)

        if i in left_list :
            result = "L"
            left_hand_pos = dist_pos
        elif i in right_list :
            result = "R"
            right_hand_pos = dist_pos
        else :
            left_dist = calculateDistance(left_hand_pos, dist_pos)
            right_dist = calculateDistance(right_hand_pos, dist_pos)

            if left_dist > right_dist:
                right_hand_pos = dist_pos
                result = "R"
            elif left_dist < right_dist :
                left_hand_pos = dist_pos
                result = "L"
            else :
                if hand == "right" :
                    right_hand_pos = dist_pos
                    result = "R"
                else :
                    left_hand_pos = dist_pos
                    result = "L"
        answer.append(result)

        # print("--------------------")
        # print(i)
        # print(dist_pos)
        # print(left_hand_pos)
        # print(right_hand_pos)
        # print(result)
        # print("--------------------")

    answer = "".join(answer)
    return answer


numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = "right"

# print(findPosition("*"))
print(solution(numbers, hand))
