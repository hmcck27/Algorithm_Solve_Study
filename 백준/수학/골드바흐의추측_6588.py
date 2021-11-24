import sys

nums = list()
while True:
    num = int(sys.stdin.readline().rstrip())
    if num == 0:
        break
    else:
        nums.append(num)

max_value = 1000000

a = [False,False] + [True]*(max_value-1)
primes = set()

for i in range(2, max_value+1):
    if a[i]:
        primes.add(i)
        for j in range(2*i, max_value+1, i):
            a[j] = False

for i in nums:
    flag = False
    fir = 2
    sec = max_value - 2
    for j in primes:
        if i - j in primes:
            flag = True
            print(f"{i} = {j} + {i-j}")
            break
    if not flag:
        print("Goldbach's conjecture is wrong.")




