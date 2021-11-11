import sys

class Queue():
    def __init__(self):
        self.list = list()
        self.size = 0

    def push(self, value):
        self.list.append(value)
        self.size += 1

    def pop(self):
        if self.size == 0:
            return -1
        else:
            self.size -= 1
            return self.list.pop(0)


    def empty(self):
        if self.size == 0:
            return 1
        else:
            return 0

    def front(self):
        if self.size == 0:
            return -1
        else:
            return self.list[0]

    def back(self):
        if self.size == 0:
            return -1
        else:
            return self.list[-1]

queue = Queue()
n = int(sys.stdin.readline().rstrip())
answer = list()
for i in range(n):
    commands = sys.stdin.readline().rstrip().split()
    if commands[0] == "push":
        queue.push(commands[1])
    elif commands[0] == "front":
        answer.append(queue.front())
    elif commands[0] == "back":
        answer.append(queue.back())
    elif commands[0] == "size":
        answer.append(queue.size)
    elif commands[0] == "empty":
        answer.append(queue.empty())
    elif commands[0] == "pop":
        answer.append(queue.pop())


for i in answer:
    print(i)