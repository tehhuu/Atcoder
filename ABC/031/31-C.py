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

N = ii()
A = li()

ans = -float('inf')
for i in range(N):
    max_b = -float('inf')
    for j in range(N):
        if i == j:
            continue
        small = min(i, j)
        big = max(i, j)
        b = sum(A[small+1 : big+1 : 2])
        if b > max_b:
            ind_b = j
            max_b = b
    max_a = sum(A[min(i, ind_b) : max(i, ind_b)+1 : 2])
    ans = max(ans, max_a)    
        
print(ans)