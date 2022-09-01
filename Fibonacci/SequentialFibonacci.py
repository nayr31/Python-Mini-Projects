# Recursion is stupid! Iteration is the best method indeed...

cache = [0, 1]

def fib(n):
    for i in range(n+1):
        if i not in {0, 1}:
            b = cache[i-1] + cache[i-2]
            cache.append(b)
    return cache[n]

x = 100

import time

tic = time.perf_counter()
ans = fib(x)
toc = time.perf_counter()

print(f"Got {ans} as the {x}th fibonacci number in " + str(toc-tic) + "ms.")
print(cache)