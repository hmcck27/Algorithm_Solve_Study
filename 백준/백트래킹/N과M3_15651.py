import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

def pick(n, picked, toPick):
    if toPick == 0:
        for i in picked:
            print(i+1, end=' ')
        print('')
    else :
        for i in range(0, n):
            picked.append(i)
            pick(n, picked, toPick-1)
            picked.pop()

pick(n, [], m)