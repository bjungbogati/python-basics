import timeit

def memoize(f):
    cache = {}
    def func(x):
        if x not in cache:            
            cache[x] = f(x)
        return cache[x]
    return func

def sum(n):
    if n <= 1:
        return n
    else:
        return n + sum(n-1)
    
sum = memoize(sum)

print("Sum of Natural Number :", sum(299))
print("Time taken:", timeit.timeit('sum(299)', globals=globals(), number=1))

