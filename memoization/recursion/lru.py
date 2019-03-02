import functools, timeit

@functools.lru_cache(maxsize=128)

def sum(n):
    if n <= 1:
        return n
    else:
        return n + sum(n-1)
    

print("Sum of Natural Number :", sum(299))
print("Time taken:", timeit.timeit('sum(299)', globals=globals(), number=1))

