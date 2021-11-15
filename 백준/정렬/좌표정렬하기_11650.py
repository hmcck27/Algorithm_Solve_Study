import sys

N = int(sys.stdin.readline().rstrip())
array = list()
for i in range(N):
    array.append(list(map(int, sys.stdin.readline().rstrip().split())))

def first_element(array):
    return array[0]

def second_element(array):
    return array[1]

def left_bigger_sort(array1, array2):

    '''
        왼쪽 원소가 더 크면 True
    '''

    if first_element(array1) > first_element(array2):
        return True
    elif first_element(array1) == first_element(array2):
        if second_element(array1) > second_element(array2):
            return True
        elif second_element(array1) == second_element(array2):
            return 'Same'
        else:
            return False
    else :
        return False

def merge(left, right):

    left_index = 0
    right_index = 0

    result_array = list()

    while left_index <= len(left)-1 and right_index <= len(right)-1:



        result = left_bigger_sort(left[left_index], right[right_index])

        if result == False:
            result_array.append(left[left_index])
            left_index += 1
        elif result == True:
            result_array.append(right[right_index])
            right_index += 1

        elif result == "Same" :
            result_array.append(right[right_index])
            right_index += 1
            result_array.append(left[left_index])
            left_index += 1

    while left_index <= len(left) -1:
        result_array.append(left[left_index])
        left_index += 1

    while right_index <= len(right) - 1:
        result_array.append(right[right_index])
        right_index += 1

    return result_array

def merge_sort(array, left_index, right_index):

    if right_index <= left_index:
        return array[left_index:right_index+1]

    middle_index = (left_index + right_index) // 2 + 1

    left_list = merge_sort(array, left_index, middle_index-1)
    right_list = merge_sort(array, middle_index, right_index)

    result_list = merge(left_list, right_list)

    return result_list


result = merge_sort(array,0,len(array)-1)
for i in result :
    print(i[0],i[1])

