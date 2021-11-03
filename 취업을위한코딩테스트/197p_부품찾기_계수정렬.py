import sys

n = int(sys.stdin.readline().rstrip())

count_array = [0] * 1000000

array = list(map(int, sys.stdin.readline().rstrip().split()))
m = int(sys.stdin.readline().rstrip())
target_list = list(map(int, sys.stdin.readline().rstrip().split()))

for i in array:
    count_array[int(i)] += 1

for i in target_list:
    if count_array[int(i)] != 0 :
        print('yes', end = ' ')
    else :
        print('no', end = ' ')
