def binary_search(array, target, start, end):

    while start <= end:
        middle = (start + end) // 2
        if array[middle] == target:
            return middle
        else :
            if array[middle] > target :
                end = middle-1
            else :
                start = middle+1

    return None

n, target = map(int, input().split())
array = [ int(j) for j in input().split()]
print(array)
result = binary_search(array, target, 0, n-1)
if result == None:
    print("해당 원소가 없습니다.")
else :
    print(result + 1)

