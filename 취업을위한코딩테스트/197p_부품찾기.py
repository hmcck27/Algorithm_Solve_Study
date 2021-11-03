import sys

n = int(sys.stdin.readline().rstrip())
array = list(map(int, sys.stdin.readline().rstrip().split()))
m = int(sys.stdin.readline().rstrip())
target_list = list(map(int, sys.stdin.readline().rstrip().split()))

print(n, m, array, target_list)

def binary_search(array, target, start, end):
    if start > end :
        return None
    middle = (start + end) // 2
    if array[middle] == target:
        return middle

    if array[middle] > target :
        return binary_search(array, target, start, middle-1)
    else :
        return binary_search(array, target, middle+1, end)

array.sort()

for i in target_list :
    result = binary_search(array, i, 0, n-1)
    if result != None:
        print('yes', end=' ')
    else :
        print('no', end = ' ')