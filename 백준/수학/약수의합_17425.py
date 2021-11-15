from sys import stdin

input = stdin.readline

Max = 1000000

ans = list()

G = [0] * 1000001
F = [1] * 1000001

def calculate_gx():
    for i in range(2, Max+1):
        for j in range(i, Max+1, i):
            F[j] += i

    for i in range(1, Max+1):
        G[i] = G[i-1] + F[i]

calculate_gx()


n = int(input().strip())
for _ in range(n):
    ans.append(G[int(input().rstrip())])

for k in ans:
    print(k)



