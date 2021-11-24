import sys
from enum import Enum

class Bigger(Enum):
    left = 1
    right = 2
    same = 3


N = int(sys.stdin.readline().rstrip())
word_list = list()

for i in range(N):
    word_list.append(sys.stdin.readline().rstrip())

def which_one_small(word1, word2):

    if len(word1) < len(word2):
        return Bigger.left
    elif len(word1) > len(word2):
        return Bigger.right
    else:
        if word1 < word2:
            return Bigger.left
        elif word1 > word2:
            return Bigger.right
        else:
            return Bigger.same



def merge(left, right):

    left_index = 0
    right_index = 0
    result_list = list()

    while left_index <= len(left)-1 and right_index <= len(right)-1:
        if which_one_small(left[left_index], right[right_index]) == Bigger.left:
            result_list.append(left[left_index])
            left_index+=1
        elif which_one_small(left[left_index], right[right_index]) == Bigger.right:
            result_list.append(right[right_index])
            right_index += 1
        elif which_one_small(left[left_index], right[right_index]) == Bigger.same:
            result_list.append(right[right_index])
            right_index += 1
            left_index += 1

    while left_index <= len(left) - 1:
        result_list.append(left[left_index])
        left_index += 1

    while right_index <= len(right) - 1:
        result_list.append(right[right_index])
        right_index += 1

    return result_list

def merge_sort(word_list, left_index, right_index):

    if left_index >= right_index:
        return word_list[left_index:right_index+1]

    middle_index = (left_index + right_index) // 2

    left_list = merge_sort(word_list, left_index, middle_index)
    right_list = merge_sort(word_list, middle_index+1, right_index)

    return merge(left_list, right_list)

result = merge_sort(word_list, 0, len(word_list)-1)

for i in result:
    print(i)
