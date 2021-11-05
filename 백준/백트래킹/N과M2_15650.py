import sys
n,m = map(int, sys.stdin.readline().rstrip().split())

def pick(n, picked, toPick):
    if toPick == 0:
        for i in picked:
            print(i+1, end=' ')
        print("")
    else :
        smallest = 0 if len(picked) == 0 else picked[-1]+1
        for i in range(smallest, n):
            picked.append(i)
            pick(n, picked,toPick-1)
            picked.pop()

pick(n, [], m)

