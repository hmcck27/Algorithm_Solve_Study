import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
array = list()
for i in range(n):
    array.append(int(sys.stdin.readline().rstrip()))

i = 1
stack = deque()
start = 1
answer = list()
flag = 0

for i in array:
    while start <= i:
        stack.append(start)
        answer.append("+")
        start += 1
    if len(stack) != 0 and stack[-1] == i:
        stack.pop()
        answer.append("-")
    elif start > i:
        flag = 1
        break

if flag == 1:
    print("NO")
else:
    for i in answer:
        print(i)