import sys

def recursion(idx, sum_value, idxStack):
    global max_value

    if max_value < sum_value:
        max_value = sum_value

    for i in range(idx, len(tList)):
        if i not in idxStack and i + tList[i] <= len(tList):
            idxStack.append(i)
            sum_value += pList[i]
            recursion(i + tList[i], sum_value, idxStack)
            idxStack.pop()
            sum_value -= pList[i]

if __name__ == "__main__":
    n = int(sys.stdin.readline().rstrip())
    tList = list()
    pList = list()
    max_value = 0
    for i in range(n):
        t, p = map(int, sys.stdin.readline().strip().split())
        tList.append(t)
        tList.append(p)
    recursion(0, 0, [])
    print(max_value)