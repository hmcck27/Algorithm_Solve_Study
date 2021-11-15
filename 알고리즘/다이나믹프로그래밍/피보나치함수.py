'''

    recursive

'''

def fibo(n):
    if n == 2 or n == 1:
        return 1

    return fibo(n-2) + fibo(n-1)

print(fibo(4))