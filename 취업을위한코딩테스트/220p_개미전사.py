from sys import stdin
input = stdin.readline

n = int(input().rstrip())
array = list(map(int, input().rstrip().split()))

d = [0] * 100
d[0] = array[0]
d[1] = array[1]

for i in range(2,len(array)):
    if array[i] + d[i-2] > d[i-1]:
        d[i] = array[i] + d[i-2]
    else:
        d[i] = d[i - 1]

print(d[n-1])