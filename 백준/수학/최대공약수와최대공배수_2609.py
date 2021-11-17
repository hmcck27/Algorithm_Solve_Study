import sys

n,m = map(int, sys.stdin.readline().rstrip().split())


max_value = max(n,m)
min_ = 1
max_ = 1
for i in range(2, max_value+1):
    if n % i == 0 and m % i == 0:
        if i >= min_:
            min_ = i

print(min_)

start1 = 1
start2 = 1
result = None

while True:
    if n * start1 == m * start2:
        result = n * start1
        break
    elif n * start1 < m * start2:
        start1 += 1
    elif n * start1 > m * start2:
        start2 += 1

print(result)