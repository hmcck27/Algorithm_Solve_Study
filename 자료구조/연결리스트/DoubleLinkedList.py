class Node(object):
    def __init__(self, data, next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev

class DoubleLinkedList(object):

    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.size = 0

    def listSize(self):
        return self.size

    def is_empty(self):
        if self.size == 0:
            return True
        else:
            return False

    def selectNode(self, idx):
        if self.is_empty():
            print("list is empty")
            return None
        elif idx >= self.size//2:




