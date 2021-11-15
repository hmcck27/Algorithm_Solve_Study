class Node(object):
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class CircularLinkedList(object):
    def __init__(self):
        self.head = Node(None)
        self.head.next = self.head
        self.size = 0

    def listsize(self):
        return self.size

    def is_empty(self):
        if self.size == 0:
            return True
        else:
            return False

    def insert(self, value, idx):
        if idx >= self.size:
            print("wrong idx")
            return None
        else:
            newNode = Node(value)
            target = self.selectNode(idx-1)
            target_next = target.next
            newNode.next = target_next
            target.next = newNode
            self.size+=1

    def delete(self, idx):
        if idx >= self.size:
            print("wrong idx")
            return None
        else:
            target_prev = self.selectNode(idx-1)
            target = target_prev.next
            target_next = target.next
            del target
            target_prev.next = target_next

    def printlist(self):
        start = self.head.next
        for _ in range(self.size-1):
            print(start, end ="=")
        print("")

    def appendLeft(self, value):
        if self.size == 0:
            newNode = Node(value)
            self.head.next = newNode
            newNode.next = self.head.next
        else:
            target = self.head.next
            newNode = Node(value)
            self.head.next = newNode
            newNode.next = target

    def append(self, value):
        if self.size == 0:
            newNode = Node(value)
            self.head.next = newNode
            newNode.next = self.head.next
        else:
            target = self.selectNode(self.size-1)
            target.next = Node(value, self.head.next)

    def selectNode(self, idx):
        if self.is_empty():
            print("list is empty")
            return None
        else:
            target = self.head.next
            for _ in range(idx):
                target = target.next
            return target




