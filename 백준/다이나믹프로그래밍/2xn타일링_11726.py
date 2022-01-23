import sys

def dpTile(n):

    for i in range(2, n+1):
        d[i] = d[i-2] + d[i-1]

if __name__ == "__main__":
    n = int(sys.stdin.readline().rstrip())
    d = [0] * 1001
    d[1] = 1
    d[0] = 1
    dpTile(n)
    # print(d)
    print(d[n]%10007)
