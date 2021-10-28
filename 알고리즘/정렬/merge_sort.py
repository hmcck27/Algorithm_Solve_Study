## selection sort

import random
import time


def check_sorted(sequence, N):
    for i in range(N - 1):
        if sequence[i] > sequence[i + 1]:
            return False
    return True


def merge(left, right):

    left_index = 0
    right_index = 0

    result_list = list()

    while left_index != len(left) - 1 and right_index != len(right) - 1:

        if left[left_index] > right[right_index]:
            result_list.append(right[right_index])
            right_index += 1

        elif left[left_index] < right[right_index]:
            result_list.append(left[left_index])
            left_index += 1

        else:
            result_list.append(left[left_index])
            result_list.append(right[right_index])
            left_index += 1
            right_index += 1

    while left_index < len(left) - 1:
        result_list.append(left[left_index])
        left_index += 1
    while right_index < len(right) - 1:
        result_list.append(right[right_index])
        right_index += 1

    return result_list

def merge_sort(sequence, left, right, leftList, rightList):
    # divide and conquer

    print(left, right)
    if abs(right - left) <= 1:
        return sequence[left: right]

    middle = (right-left) // 2

    leftList = merge_sort(sequence, left, middle, leftList)
    rightList = merge_sort(sequence, middle+1, right, rightList)

    result_list = merge(leftList, rightList)

    print(leftList)
    print(rightList)
    print(result_list)
    return result_list

## make random integer sequence
print("making random sequence...")
# N = random.randint(1, 100)
# sequence = list()
# for i in range(N):
#     sequence.append(random.randint(-10000000, 10000000))
N = 11
sequence = [5, 3, 8, 10, 10, 4, 9, 1, 6, 2, 7]

# sort start
start = time.time()

print("now sorting...")
merge_sort(sequence, 0, N - 1, sequence[0:int(N-1)//2], sequence[int(N-1)//2:N])

end = time.time()

## check result of sort function
if check_sorted(sequence, N):
    print("정럴이 잘 되었습니다.")
else:
    print("정렬이 잘 되지 않았습니다.")

print("start : ", start)
print("end : ", end)
print("size of sequence : ", N)
print("time ratio ( size(sequence) / (end-start) ) : ", N / (end - start))
