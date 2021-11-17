from sys import stdin

def check(picked):
    sum = 0
    for i in picked:
        sum += array[i]
    if sum == 100:
        return True
    else:
        return False

result = list()

def pick(n, picked, toPick):
    if toPick == 0:
        if check(picked) and result == []:
            for i in picked:
                result.append(array[i])
            result.sort()
            for i in result:
                print(i)
    else:
        smallest = 0 if len(picked) == 0 else picked[-1] + 1
        for next in range(smallest, n):
            picked.append(next)
            pick(n, picked, toPick-1)
            picked.pop()

array = list()

for _ in range(9):
    array.append(int(stdin.readline().rstrip()))

pick(9, [], 7)


