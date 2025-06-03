import time
from datetime import timedelta
from functools import lru_cache

def recursive_factorial(n):
    if n == 1:
        return 1
    else:
        return n * recursive_factorial(n - 1)
    
@lru_cache
def cached_factorial(n):
    return recursive_factorial(n)

def main():
    n = 20

    start_time = time.time()
    print(f"Recursive factorial of {n}: {recursive_factorial(n)}")
    duration = timedelta(time.time() - start_time)
    print(f"Calculation time without caching: {duration}")

    start_time = time.time()
    print(f"Cached factorial of {n}: {cached_factorial(n)}")
    duration = timedelta(time.time() - start_time)
    print(f"Calculation time with caching: {duration}")

    start_time = time.time()
    print(f"Cached factorial of {n}, repeated: {cached_factorial(n)}")
    duration = timedelta(time.time() - start_time)
    print(f"Second calculation time with caching: {duration}")


if __name__ == "__main__":
    main()