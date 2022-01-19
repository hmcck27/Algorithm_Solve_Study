import sys
n = int(sys.stdin.readline())
array = list()
for i in range(n):
    array.append(int(sys.stdin.readline()))

count = 0

def recursive_div(n):
    global count
    if n == 1:
        count += 1
        return
    elif n == 2:
        count += 2
        return
    elif n == 3:
        count += 4
        return
    else:
        recursive_div(n-1)
        recursive_div(n-2)
        recursive_div(n-3)

for i in array:
    count = 0
    recursive_div(i)
    print(count)
