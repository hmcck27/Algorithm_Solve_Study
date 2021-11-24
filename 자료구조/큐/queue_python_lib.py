from collections import deque

queue = deque()

queue.append(5)
queue.append(2)
queue.popleft()

print(queue)