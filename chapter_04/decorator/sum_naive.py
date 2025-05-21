def number_sum(n):
    if n == 0:
        return 0
    else:
        return n + number_sum(n - 1)
    
if __name__ == "__main__":
    from timeit import Timer

    t = Timer("number_sum(50)", "from __main__ import number_sum")
    print("Time: ", t.timeit())