class Queue():

    def __init__(self):
        self.queue = list()
        self.count = 0

    def push(self, data):
        data = list(data)
        data += self.queue
        self.queue = data
        self.count += 1

    def pop(self):
        pop_object = None

        if self.queue.isEmpty():
            print("queue is empty")
        else :
            self.count -= 1
            pop_object = self.queue.pop()

        return pop_object

    def top(self):
        top_object = None
        if self.queue.isEmpty():
            print("queue is empty")
        else:
            top_object = self.queue[-1]

        return top_object

    def count(self):
        return self.count

    def isEmpty(self):
        if len(self.queue) == 0:
            return True
        else:
            return False

