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
        self.tail.prev = self.head
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
        if idx > self.size:
            print("idx is wrong")
            return None
        elif idx < self.size//2:
            target = self.head.next
            for _ in range(idx):
                target = target.next
            return target
        else:
            target = self.tail.prev
            for _ in range(self.size - idx - 1):
                target = target.prev
            return target

    def appendleft(self, value):
        if self.is_empty():
            newNode = Node(value)
            self.head.next = newNode
            newNode.prev = self.head
            newNode.next = self.tail
            self.tail.prev = newNode
        else:
            newNode = Node(value)
            tmp = self.head.next
            newNode.prev = self.head
            tmp.prev = newNode
            newNode.next = tmp
            self.head.next = newNode

        self.size += 1

    def append(self, value):
        if self.is_empty():
            newNode = Node(value)
            self.head.next = newNode
            newNode.prev = self.head
            newNode.next = self.tail
            self.tail.prev = newNode
        else:
            tmp = self.tail.prev
            newNode = Node(value)
            newNode.prev = tmp
            newNode.next = self.tail
            tmp.next = newNode
            self.tail.prev = newNode
        self.size += 1

    def insert(self, value, idx):
        if self.size <= idx:
            print("wrong idx")
            return None
        else:
            newNode = Node(value)
            target_prev = self.selectNode(idx).prev
            target_next = target_prev.next
            newNode.prev = target_prev
            newNode.next = target_next
            target_prev.next = newNode
            target_next.prev = newNode
            self.size += 1


    def delete(self,idx):
        if self.is_empty():
            print("list is empty")
            return None
        elif self.size <= idx:
            print("idx is wrong")
            return None
        else:
            target = self.selectNode(idx)
            previous = target.prev
            next = target.next
            del target
            previous.next = next
            next.prev = previous
        self.size -= 1

    def printlist(self):
        if self.is_empty():
            print("list is empty")
            return None
        else:
            target = self.head.next
            while target != self.tail:
                print(target.data, end="= ")

                target = target.next
            print("")

mylist = DoubleLinkedList()
mylist.append('A')
mylist.printlist()
mylist.append('B')
mylist.printlist()
mylist.append('C')
mylist.printlist ()
mylist.insert('D', 1)
mylist.printlist()
mylist.appendleft('E')
mylist.printlist()
print(mylist.listSize())
mylist.delete(0)
mylist.printlist()
mylist.delete(3)
mylist.printlist()
mylist.delete(0)
mylist.printlist()
mylist.appendleft('A')
mylist.printlist()
