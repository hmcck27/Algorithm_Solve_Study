import sys

class Stack():
    def __init__(self):
        self.stack = list()
        self.count = 0

    def push(self,data):
        self.stack.append(data)
        self.count += 1

    def top(self):
        if self.count == 0:
            return -1
        return self.stack[-1]

    def size(self):
        return self.count

    def empty(self):
        if self.count == 0:
            return 1
        else: return 0

    def pop(self):
        if self.count == 0:
            return -1
        else:
            self.count -= 1
            return self.stack.pop(-1)


stack = Stack()
N = int(sys.stdin.readline().rstrip())

commands = []
for i in range(N):
    commands.append(sys.stdin.readline().rstrip().split())

for i in range(N):
    command = commands[i][0]
    if command == "push":

        data = int(commands[i][1])
        stack.push(data)
    elif command == "pop":
        print(stack.pop())
    elif command == "top":
        print(stack.top())
    elif command == "size":
        print(stack.size())
    elif command == "empty":
        print(stack.empty())
