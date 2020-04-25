import sys
sys.setrecursionlimit(10**8)
def ii(): return int(sys.stdin.readline())
def mi(): return map(int, sys.stdin.readline().split())
def li(): return list(map(int, sys.stdin.readline().split()))
def li2(N): return [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
def dp2(ini, i, j): return [[ini]*i for _ in range(j)]
def dp3(ini, i, j, k): return [[[ini]*i for _ in range(j)] for _ in range(k)]
import bisect #bisect.bisect_left(B, a)
#from collections import defaultdict #d = defaultdict(int) d[key] += value
#from itertools import accumulate #list(accumulate(A))

N = ii()
A = [ii() for _ in range(N)]

dp = [float('inf') for _ in range(N)]

for i in range(N):
    ind = bisect.bisect_left(dp, A[i])
    dp[ind] = min(A[i], dp[ind])

for i in range(N-1):
    if dp[i+1] == float('inf'):
        print(i+1)
        exit()
print(N)






