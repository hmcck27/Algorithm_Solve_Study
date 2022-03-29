from itertools import permutations
import re

def solution(expression):
    p = permutations(["*", "-", "+"], 3)
    p = list(p)

    # expression 에서 숫자랑 연산자 분리하기
    operand = re.findall(r'[0-9]+', expression)
    operate = re.findall(r'[*|\-|+]+', expression)

    ex = []
    for i in range(len(operand) - 1):
        ex.extend([int(operand[i]), operate[i]])
    ex.extend([operand[i+1]])

    max_value = None

    for rank in p:
        temp = ex[:]
        for op in rank:
            temp= calculate(temp, op)
        value = abs(temp[0])
        if max_value == None:
            max_value = value
        else:
            if max_value < value:
                max_value = value

    return max_value

def calculate(ex, op):
    # ex 식에서 op 연산자만 계산해서 리스트 재구성해서 반환
    temp = []

    i = 0
    while i < len(ex)-2:
        if i >= len(ex)-2:
            break
        if ex[i+1] == op:
            operend1 = ex[i]
            operend2 = ex[i+2]
            if op == "*":
                result = int(operend1) * int(operend2)
            elif op == "-":
                result = int(operend1) - int(operend2)
            else:
                result = int(operend1) + int(operend2)
            del ex[i:i+3]
            ex.insert(i, result)
            i -= 1
        i += 1

    return ex



if __name__ == "__main__":
    # expression = "100-200*300-500+20"
    expression = "50*6-3*2"
    print(solution(expression))