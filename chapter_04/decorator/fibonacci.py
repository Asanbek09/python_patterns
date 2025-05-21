fib_cache = {0: 0, 1: 1}

def fibonacci(n):
    if n in fib_cache:
        return fib_cache[n]
    
    res = fibonacci(n - 1) + fibonacci(n - 2)
    fib_cache[n] = res
    return res