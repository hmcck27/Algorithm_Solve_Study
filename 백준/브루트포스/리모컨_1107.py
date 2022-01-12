import sys

num = sys.stdin.readline().rstrip()
num_int = int(num)
num_list = list()
for i in range(len(num)):
    num_list.append(int(num[i]))

n = int(sys.stdin.readline().rstrip())

key = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

if n != 0:
    un_key = list(map(int, sys.stdin.readline().rstrip().split()))
    for _ in un_key:
        key.remove(_)

start = 100
result_set = set()
result_set.add(abs(100-num_int))
result_list = list()

min_value = abs(100-num_int)

def transform(stack_list):

    result = 0

    for i in range(len(stack_list)):
        result += stack_list[i] * 10**(len(stack_list)-i-1)

    return result

def check(stack_list):

    global min_value

    if len(stack_list) > 6 :
        return
    else :
        for i in range(len(key)):
            stack_list.append(key[i])
            if min_value > abs(num_int - transform(stack_list)) + len(stack_list):
                min_value = abs(num_int - transform(stack_list)) + len(stack_list)
            check(stack_list)
            stack_list.pop(-1)

check([])

print(min_value)







