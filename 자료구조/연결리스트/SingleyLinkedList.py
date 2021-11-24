class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class SingleLinkedList(object):
    def __init__(self):
        self.head = Node(None)
        self.size = 0

    def listSize(self):
        return self.size

    def is_empty(self):
        if self.size == 0:
            return True
        else:
            return False

    def selectNode(self, idx):
        if idx > self.size:
            print("index error")
            return None
        elif idx == 0:
            return self.head
        else:
            target = self.head
            for cnt in range(idx):
                target = target.next
            return target

    def appendleft(self,value):
        if self.is_empty():
            self.head = Node(value)
        else:
            self.head = Node(value, self.head)
        self.size += 1

    def append(self,value):
        if self.is_empty():
            self.head = Node(value)
        else:
            target = self.head
            while target.next != None:
                target = target.next
            newTail = Node(value)
            target.next = newTail
        self.size += 1

    def insert(self,value, idx):
        if self.is_empty():
            self.head = Node(value)
            self.size += 1
        elif idx == 0:
            self.head = Node(value, self.head)
            self.size += 1
        elif idx >= self.size:
            print("idx error")
            return None
        else :
            target = self.selectNode(idx-1)
            target.next = Node(value, target.next)
            self.size += 1

    def delete(self, idx):
        if self.is_empty():
            print("idx error!")
            return None
        elif idx >= self.size:
            print("Overflow idx error")
            return None
        elif idx == 0:
            target = self.head
            self.head = target.next
            del(target)
            self.size -= 1
        else:
            target = self.selectNode(idx-1)
            delTarget = target.next
            target.next = delTarget.next
            del(delTarget)
            self.size -= 1

    def printlist(self):
        target = self.head
        while target.next != None:
            print(target.data, end='')
            target = target.next
        print(target.data)

mylist = SingleLinkedList()
mylist.append('A')
mylist.printlist()
mylist.append('B')
mylist.printlist()
mylist.append('C')
mylist.printlist()
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
