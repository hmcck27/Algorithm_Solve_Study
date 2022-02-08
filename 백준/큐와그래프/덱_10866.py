"""


시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
0.5 초 (추가 시간 없음)	256 MB	38778	20979	17742	56.149%
문제
정수를 저장하는 덱(Deque)를 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

명령은 총 여덟 가지이다.

push_front X: 정수 X를 덱의 앞에 넣는다.
push_back X: 정수 X를 덱의 뒤에 넣는다.
pop_front: 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
pop_back: 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 덱에 들어있는 정수의 개수를 출력한다.
empty: 덱이 비어있으면 1을, 아니면 0을 출력한다.
front: 덱의 가장 앞에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
back: 덱의 가장 뒤에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
입력
첫째 줄에 주어지는 명령의 수 N (1 ≤ N ≤ 10,000)이 주어진다. 둘째 줄부터 N개의 줄에는 명령이 하나씩 주어진다. 주어지는 정수는 1보다 크거나 같고, 100,000보다 작거나 같다. 문제에 나와있지 않은 명령이 주어지는 경우는 없다.

출력
출력해야하는 명령이 주어질 때마다, 한 줄에 하나씩 출력한다.
"""

class Deque():

    deque = None
    length = None

    def __init__(self):
        self.deque = list()
        self.length = 0

    def push_front(self, x):
        self.deque = [x] + self.deque
        self.length += 1

    def push_back(self, x):
        self.deque.append(x)
        self.length += 1

    def pop_front(self):
        if self.is_empty():
            print(-1)
        else:
            print(self.deque[0])
            self.deque = self.deque[1:]
            self.length -= 1

    def pop_back(self):
        if self.is_empty():
            print(-1)
        else:
            print(self.deque.pop())
            self.length -= 1

    def size(self):
        print(len(self.deque))

    def is_empty(self):
        if len(self.deque) == 0:
            return 1
        else:
            return 0

    def empty(self):
        if self.is_empty():
            print(1)
        else:
            print(0)

    def front(self):
        if self.is_empty():
            print(-1)
        else:
            print(self.deque[0])

    def back(self):
        if self.is_empty():
            print(-1)
        else:
            print(self.deque[-1])



if __name__ == "__main__":
    import sys
    n = int(sys.stdin.readline().rstrip())
    commandList = []
    for i in range(n):
        commandList.append(list(sys.stdin.readline().rstrip().split()))

    deque = Deque()

    for i in commandList:
        if i[0] == "push_back":
            deque.push_back(i[1])
        elif i[0] == "push_front":
            deque.push_front(i[1])
        elif i[0] == "front":
            deque.front()
        elif i[0] == "back":
            deque.back()
        elif i[0] =="size":
            deque.size()
        elif i[0] == "empty":
            deque.empty()
        elif i[0] == "pop_front":
            deque.pop_front()
        elif i[0] == "pop_back":
            deque.pop_back()



