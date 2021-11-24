def binary_search(array, target, start, end):
    if start > end:
        return None
    middle_index = (start+end)//2
    if array[middle_index] == target :
        return middle_index
    else :
        if array[middle_index] > target:
            return binary_search(array, target, start, middle_index-1)
        elif array[middle_index] < target:
            return binary_search(array, target, middle_index+1, end)

n, target = map(int, input().split())
array = [ int(j) for j in input().split()]
print(array)
result = binary_search(array, target, 0, n-1)
if result == None:
    print("해당 원소가 없습니다.")
else :
    print(result + 1)

