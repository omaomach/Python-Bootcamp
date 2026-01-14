import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"{func.__name__} took {time.time() - start} seconds")
        return result
    return wrapper

@timer
def calculate_sum(n):
    return sum(range(n))

print(calculate_sum(1000000))