sum_cache = {0: 0}

def number_sum(n):
    if n in sum_cache:
        return sum_cache[n]
    res = n + number_sum(n - 1)
    sum_cache[n] = res
    return res

fib_cache = {0: 0, 1: 1}

def fibonacci(n):
    if n in fib_cache:
        return fib_cache[n]
    
    res = fibonacci(n - 1) + fibonacci(n - 2)
    fib_cache[n] = res
    return res

if __name__ == "__main__":
    from timeit import Timer

    t = Timer(
        "fibonacci(100)",
        "from __main__ import fibonacci",
    )
    print("Time: ", t.timeit())