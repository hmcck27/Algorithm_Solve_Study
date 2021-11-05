import sys
from enum import Enum

class first(Enum):
    left = 1
    right = 2
    same = 3

N = int(sys.stdin.readline().rstrip())
array = list()

for i in range(N):
    input_ = sys.stdin.readline().rstrip().split()
    input_[0] = int(input_[0])
    input_.append(i)
    array.append(input_)

def which_one_first(left, right):

    if left[0] < right[0]:
        return first.left
    elif left[0] > right[0]:
        return first.right
    else:
        if left[2] < right[2]:
            return first.left
        elif left[2] > right[2]:
            return first.right
        else:
            return first.same

def merge(left, right):

    left_index= 0
    right_index = 0

    result_list = list()

    while left_index <= len(left)-1 and right_index <= len(right)-1 :
        if which_one_first(left[left_index], right[right_index]) == first.left:
            result_list.append(left[left_index])
            left_index += 1
        elif which_one_first(left[left_index], right[right_index]) == first.right:
            result_list.append(right[right_index])
            right_index += 1
        else:
            result_list.append(left[left_index])
            left_index += 1
            result_list.append(right[right_index])
            right_index += 1

    while left_index <= len(left) -1:
        result_list.append(left[left_index])
        left_index += 1

    while right_index <= len(right) - 1:
        result_list.append(right[right_index])
        right_index += 1

    return result_list

def merge_sort(array, left_index, right_index):

    if left_index >= right_index:
        return array[left_index: right_index+1]

    middle_index= (left_index + right_index) // 2

    left_list = merge_sort(array, left_index, middle_index)
    right_list = merge_sort(array, middle_index+1, right_index)

    return merge(left_list, right_list)


result = merge_sort(array, 0, len(array)-1)


for i in result:
    print(i[0], i[1])