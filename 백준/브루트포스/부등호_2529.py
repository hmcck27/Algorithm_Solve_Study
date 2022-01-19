import sys

def isPos(i, array):
    if len(array) == 0:
        return True
    operator = eList[len(array)-1]
    if operator == ">":
        if array[-1] > i:
            return True
        else:
            return False
    elif operator == "<":
        if array[-1] < i:
            return True
        else:
            return False

def getEquation(left, array):

     global max_value
     global min_value
     global max_str
     global min_str

     if left == 0:
         temp = map(str, array)
         join_str = "".join(temp)
         if max_value < int(join_str):
             max_str = join_str
         if min_value > int(join_str):
             min_str = join_str

     for i in range(0, 10):
         if i not in array and isPos(i, array):
             array.append(i)
             getEquation(left-1, array)
             array.pop()

if __name__ == "__main__":
    n = int(sys.stdin.readline().rstrip())
    max_value = 0
    min_value = 9999999999
    max_str = ""
    min_str = ""
    eList = list(sys.stdin.readline().rstrip().split())
    getEquation(n+1, [])
    print(max_str)
    print(min_str)

