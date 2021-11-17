import sys
n = int(sys.stdin.readline().rstrip())

sum = 0
for i in range(1,n+1):
    sum += (n//i) * i

print(sum)

# print(sum_divisor(n))