import sys
from collections import OrderedDict

N = int(sys.stdin.readline().rstrip())

nums = list(map(int, sys.stdin.readline().rstrip().split()))
nums_set = list(set(nums))
num_dict = OrderedDict()

for i in nums:
    num_dict[i] = 0

def merge(left, right):

    left_index = 0
    right_index = 0

    result_list = list()

    while left_index <= len(left) - 1 and right_index <= len(right) - 1:
        if left[left_index] < right[right_index]:
            result_list.append(left[left_index])
            left_index+=1
        elif left[left_index] > right[right_index]:
            result_list.append(right[right_index])
            right_index += 1
        else :
            result_list.append(left[left_index])
            left_index += 1
            result_list.append(right[right_index])
            right_index += 1

    while left_index <= len(left) - 1:
        result_list.append(left[left_index])
        left_index += 1

    while right_index <= len(right) - 1:
        result_list.append(right[right_index])
        right_index += 1

    return result_list

def merge_sort(array, left_index, right_index):

    if left_index >= right_index:
        return array[left_index:right_index+1]

    middle = (left_index + right_index) // 2
    left = merge_sort(array, left_index, middle)
    right = merge_sort(array, middle+1, right_index)

    return merge(left, right)


## sort
sorted_nums = merge_sort(nums_set[:],0,len(nums)-1)
for i, v in enumerate(sorted_nums):
    num_dict[v] = i

for i in nums:
    print(num_dict[i], end=' ')



