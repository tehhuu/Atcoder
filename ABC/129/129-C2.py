import sys
from functools import lru_cache
sys.setrecursionlimit(100001)

N, M = map(int, input().split())
b = tuple([int(input()) for i in range(M)])

mod = 10**9+7

@lru_cache(maxsize=None)
def Fib(n, a):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    elif (n-2 in a) and n!=0:
        return 0
    else:
        return (Fib(n-1, a) + Fib(n-2, a)) % mod

print(Fib(N+2, b))