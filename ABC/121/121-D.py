import sys
sys.setrecursionlimit(10**8)
def ii(): return int(sys.stdin.readline())
def mi(): return map(int, sys.stdin.readline().split())
def li(): return list(map(int, sys.stdin.readline().split()))
def li2(N): return [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
def dp2(ini, i, j): return [[ini]*i for _ in range(j)]
def dp3(ini, i, j, k): return [[[ini]*i for _ in range(j)] for _ in range(k)]
#import bisect #bisect.bisect_left(B, a)
#from collections import defaultdict #d = defaultdict(int) d[key] += value
#from itertools import accumulate #list(accumulate(A))

A, B = mi()

ans = 0

def count(n):
    if n==0:
        return 0
    N = n
    n %= 4
    if n == 1:
        return 1
    if n == 2:
        return N+1
    if n == 3:
        return 0
    if n == 0:
        return N
if A > 0:
    print(count(A-1)^count(B))