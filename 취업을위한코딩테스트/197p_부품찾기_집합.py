import sys

n = int(sys.stdin.readline().rstrip())
array = set(map(int, sys.stdin.readline().rstrip().split()))
m = int(sys.stdin.readline().rstrip())
target_list = list(map(int, sys.stdin.readline().rstrip().split()))

for i in target_list:
    if i in array:
        print('yes', end = ' ')
    else :
        print('no', end = ' ')