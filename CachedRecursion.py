cache = [0, 1]

def fibb(n):
    # Return base values
    if n == 0 or n ==1: return cache[n]
    # Check for cache
    if len(cache)-1 == n:
        return cache[n]
    else:
        store = True
    
    val = fibb(n-1) + fibb(n-2)
    if store:
        if len(cache) == n:
            cache.append(val)
        else:
            cache[n] = val
    return val

x = 25
import time

tic = time.perf_counter()
for sup_n in range(x):
    f = fibb(x)
toc = time.perf_counter()
print(f"Fibonacci at {x} is {f}, done in {toc-tic}s.")
print(f"Final cache size of {len(cache)}")
print(cache)