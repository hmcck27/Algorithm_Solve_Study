class Stack():

    removeCount = 0

    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        pop_object = None
        if self.isEmpty():
            print("Stack is empty")
        else:
            return self.stack.pop()

    def top(self):
        top_object = None

        if self.isEmpty():
            print("Stack is Empty")
        else:
            top_object = self.stack[-1]

        return top_object

    def isEmpty(self):
        is_empty = None

        if len(self.stack) == 0:
            is_empty = True
        else :
            is_empty = False

        return is_empty

    def checkDouble(self):
        if len(self.stack) >= 2:
            if self.stack[-1] == self.stack[-2]:

                self.pop()
                self.pop()
                self.removeCount += 2

    def getResult(self):
        return self.removeCount

    def printStack(self):
        for i in self.stack:
            print(i)




def popFromBoard(board, pos):

    result = None

    depth = len(board)


    for j in range(depth):

        if board[j][pos-1] != 0:
            result = board[j][pos-1]
            board[j][pos-1] = 0
            return result


    result = 0
    return result


def solution(board, moves):
    answer = 0

    stk = Stack()

    for i in moves :
        from_board = popFromBoard(board, i)
        if from_board != 0:

            stk.push(from_board)
            stk.checkDouble()


    answer = stk.getResult()

    return answer


board = [[0,0,0,0,0],
         [0,0,1,0,3],
         [0,2,5,0,1],
         [4,2,4,4,2],
         [3,5,1,3,1]]

moves = [1,5,3,5,1,2,1,4]

print(solution(board, moves))