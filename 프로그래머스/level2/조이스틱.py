# coding=utf-8
'''

문제 설명
조이스틱으로 알파벳 이름을 완성하세요. 맨 처음엔 A로만 이루어져 있습니다.
ex) 완성해야 하는 이름이 세 글자면 AAA, 네 글자면 AAAA

조이스틱을 각 방향으로 움직이면 아래와 같습니다.

▲ - 다음 알파벳
▼ - 이전 알파벳 (A에서 아래쪽으로 이동하면 Z로)
◀ - 커서를 왼쪽으로 이동 (첫 번째 위치에서 왼쪽으로 이동하면 마지막 문자에 커서)
▶ - 커서를 오른쪽으로 이동
예를 들어 아래의 방법으로 "JAZ"를 만들 수 있습니다.

- 첫 번째 위치에서 조이스틱을 위로 9번 조작하여 J를 완성합니다.
- 조이스틱을 왼쪽으로 1번 조작하여 커서를 마지막 문자 위치로 이동시킵니다.
- 마지막 위치에서 조이스틱을 아래로 1번 조작하여 Z를 완성합니다.
따라서 11번 이동시켜 "JAZ"를 만들 수 있고, 이때가 최소 이동입니다.
만들고자 하는 이름 name이 매개변수로 주어질 때, 이름에 대해 조이스틱 조작 횟수의 최솟값을 return 하도록 solution 함수를 만드세요.

제한 사항
name은 알파벳 대문자로만 이루어져 있습니다.
name의 길이는 1 이상 20 이하입니다.
입출력 예
name	return
"JEROEN"	56
"JAN"	23

'''

name = "JEROEN"
# name = "JAN"


# def findNextPos(count_list, pos, n):
#
#     # 현재 위치가 pos
#     # count_list에서 0을 제회한 가장 작은 값들을 찾는다.
#     # 그리고 그 값들로 이동하는 카운트들을 구한다.
#     # 그 카운트 중에서 최소 카운트를 갖는 인덱스를 반환한다.
#
#     # 가장 작은 값 찾기
#     min_value = min(count_list)
#
#     # 여러개 일수도 있으니 리스트를 만들자
#     min_index_list = list()
#     for i in range(len(count_list)) :
#         if count_list[i] is min_value:
#             min_index_list.append(i)
#
#     # 현재 pos에서 가장 가까운 인덱스 찾기
#
#     min_count = 100
#     new_pos = pos
#
#     for i in min_index_list:
#         temp = 0
#         if abs(pos - i) > len(min_index_list)//2 :
#             temp = n - abs(pos - i)
#         else :
#             temp = abs(pos - i)
#
#         if temp < min_count:
#             min_count = temp
#             new_pos = i
#
#     return min_count, new_pos

# def moveRightLeft(count_list, n):
#     # 0을 제외하고 가장 키운트가 적은 쪽으로 이동하기
#     # count_list 의 수를 더해서 반환하는 함수
#
#     # result = 0
#     #
#     # pos = 0
#     #
#     # # 좌우로 움직여야 하는 수
#     # move_count = 0
#     # for i in count_list :
#     #     if i is not 100:
#     #         move_count += 1
#     #
#     #
#     # # move_count 만큼 반복문 돌면서 다 count_list 100 으로 만들기
#     #
#     # for i in range(move_count):
#     #     count ,pos = findNextPos(count_list, pos, n)
#     #     result += count
#     #     result += count_list[pos]
#     #     count_list[pos] = 100
#
#
#
#     return result


def findUpDownMoveCount(name):

    count_list = list()
    result = 0

    for i in name:
        ascii_count = ord(i) - 65

        if ascii_count >= 14:
            move_count = 26 - ascii_count
            count_list.append(1)
        else:
            move_count = ascii_count
            if ascii_count is not 0 :
                count_list.append(1)
            else :
                count_list.append(0)

        count_list.append(move_count)
        result += move_count

    return result, count_list

def findWayRightOrLeft(count_list):

    result_list = list()
    result_list.append(len(count_list)-1)

    for pos in range(0, len(count_list)-1) :

        if count_list[pos+1] == 0:
            zero_count = 0
            for j in range(pos+1, len(count_list)):
                if count_list[j] == 0 :
                    zero_count += 1
                else :
                    break

            if zero_count > pos and pos*2 + n - zero_count:




        present_way_count += 1




def solution(name):

    answer = 0
    answer, count_list = findUpDownMoveCount(name)
    answer += findWayRightOrLeft(count_list)

    return answer

print(solution(name))
