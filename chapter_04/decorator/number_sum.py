sum_cache = {0: 0}

def number_sum(n):
    if n in sum_cache:
        return sum_cache[n]
    
    res = n + number_sum(n - 1)
    sum_cache[n] = res
    return res

if __name__ == "__main__":
    from timeit import Timer

    t = Timer("number_sum(300)", "from __main__ import number_sum")

    print("Time:", t.timeit())