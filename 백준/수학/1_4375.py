import sys

num_list = list()

while True:
    input_ = sys.stdin.readline().rstrip()
    if input_ == "":
        break
    else:
        num_list.append(int(input_))

def find_number(i):
    start = 1
    index = 1
    while True:
        if start % i == 0:
            return index
        else:
            start = 10 * start + 1
            index += 1

for i in num_list:
    print(find_number(i))
