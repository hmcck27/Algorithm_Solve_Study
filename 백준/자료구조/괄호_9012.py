import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
word_list = list()
for i in range(n):
    word_list.append(sys.stdin.readline().rstrip())

stack = deque()

for i in word_list:
    stack = deque()
    for j in range(len(i)):
        flag = 0

        if i[j] == '(':
            stack.append(i[j])
        else :
            if len(stack) == 0:
                flag = 1
                break
            stack.pop()
    if len(stack) == 0 and flag == 0:
        print('YES')
    else:
        print('NO')
