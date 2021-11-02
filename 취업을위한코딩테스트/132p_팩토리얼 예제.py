def factorial_iterative(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

def factorial_recursive(n):

    if n <= 1 :
        return 1
    else :
        return factorial_iterative(n-1)* n

print(factorial_recursive(10))
print(factorial_iterative(10))