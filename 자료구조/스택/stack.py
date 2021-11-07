class Stack():
    def __init__(self):
        self.stack = list()
        self.count = list()

    def push(self, data):
        self.stack.append(data)
        self.count += 1

    def pop(self):
        pop_object = None
        if self.isEmpty():
            print("stack is empty")
        else:
            pop_object = self.stack.pop()
            self.count -= 1

    def isEmpty(self):
        if self.count == 0:
            return True
        else :
            return False
