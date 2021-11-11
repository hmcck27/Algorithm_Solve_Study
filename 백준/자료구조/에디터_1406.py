import sys

class Node(object):
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next


class DList(object):
    def __init__(self, word):
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
        self.cursorNode = None

        for i in range(len(word)):
            self.append(word[i])

    def printList(self):
        start = self.head.next
        while start != self.tail:
            print(start.data, end="")
            start = start.next
        print("")

    def is_empty(self):
        if self.size == 0:
            return True
        else:
            return False

    def moveLeft(self):
        if self.cursorNode == self.head:
            return None
        else:
            self.cursorNode = self.cursorNode.prev

    def moveRight(self):
        if self.cursorNode == self.tail.prev:
            return None
        else:
            self.cursorNode = self.cursorNode.next

    def append(self, value):
        if self.is_empty():
            newNode = Node(value)
            self.head.next = newNode
            self.tail.prev = newNode
            newNode.prev = self.head
            newNode.next = self.tail
            self.cursorNode = newNode
        else:
            target = self.cursorNode
            target_next = self.cursorNode.next
            newNode = Node(value)
            target.next = newNode
            newNode.prev = target
            newNode.next = target_next
            target_next.prev = newNode
            self.cursorNode = newNode
        self.size += 1

    def delete(self):
        if self.cursorNode == self.head:
            return None
        else:
            target_prev = self.cursorNode.prev
            target_next = self.cursorNode.next
            del self.cursorNode
            target_prev.next = target_next
            target_next.prev = target_prev
            self.cursorNode = target_prev
            self.size -= 1

word = sys.stdin.readline().rstrip()
n = int(sys.stdin.readline().rstrip())
commands = []

dList = DList(word)

for i in range(n):
    commands.append(sys.stdin.readline().rstrip().split())

for i in range(n):
    if commands[i][0] == "P":
        dList.append(commands[i][1])
    elif commands[i][0] == "L":
        dList.moveLeft()
    elif commands[i][0] == "D":
        dList.moveRight()
    else:
        dList.delete()

dList.printList()

