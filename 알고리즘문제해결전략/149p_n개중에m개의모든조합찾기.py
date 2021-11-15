def pick(n, picked, toPick):
    # print(n, picked, toPick)
    if toPick == 0:
        print(picked)
    else :
        smallest = 0 if len(picked) == 0 else picked[-1] + 1
        for next in range(smallest, n):
            picked.append(next)
            pick(n, picked, toPick-1)
            picked.pop()

N = [1,2,3,4]
toPick = 2

pick(4, [], toPick)
