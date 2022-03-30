from collections import deque

def divide(p):
    # 두 균형 잡힌 문자열로 반환해야 한다.
    # u는 더이상 나누는게 불가능해야 한다.

    temp = ""

    if len(p) <= 2:
        return p,""

    for i in range(len(p)-1):
        temp += p[i]

        if isBalanced(temp) and divide(temp)[0] == temp :
            return p[0:i+1], p[i+1:]

    return p,""


def isBalanced(p):
    first = 0
    second = 0
    for i in p:
        if i == ")":
            second += 1
        elif i == "(":
            first += 1

    if first == second:
        return True
    else:
        return False

def isRight(p):
    start = deque()
    end = deque()
    for i in range(len(p)-1, -1, -1):
        temp = p[i]

        if temp == ")":
            end.append(temp)
        else:
            if len(end) == 0:
                return False
            end.pop()

    if len(end) == 0:
        return True
    else:
        return False

def reverse(p):
    result = ""
    for i in p:
        if i == "(":
            result += ")"
        else:
            result += "("
    return result

def solution(p):

    if isRight(p):
        return p

    if p == "":
        return ""

    u, v = divide(p)

    temp = ""

    if isRight(u):
        temp += u
        temp += solution(v)
    else:
        temp = "("
        s = solution(v)
        temp += s
        temp += ')'
        u = u[1:-1]
        temp += reverse(u)

    return temp



if __name__ == "__main__":

    # p = "(()())()"
    # p = ")("
    # p = "()))((()"
    p = ")()(()"

    # p = "(())"
    # print(isRight(p))
    # print(divide(p))
    print(solution(p))
