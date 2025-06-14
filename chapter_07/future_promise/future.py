from concurrent.futures import ThreadPoolExecutor, as_completed

def square(x):
    return x * x

with ThreadPoolExecutor() as executor:
    future1 = executor.submit(square, 2)
    future2 = executor.submit(square, 3)
    future3 = executor.submit(square, 4)

    futures = [future1, future2, future3]

    for future in as_completed(futures):
        print(f"Result: {future.result()}")