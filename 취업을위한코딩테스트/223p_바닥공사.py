from sys import stdin
n = int(stdin.readline())

d = [0] * 1001
d[0] = 0
d[1] = 1
d[2] = 3

for i in range(3, n+1):
    d[i] = 2*d[i-2] + (d[i-1])

print(d[n]%796796)
