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

## 2015 JOI 本戦　B
## DP

N = ii()
A = [ii() for _ in range(N)]

dp = dp2(0, N, N)

for i in range(N):
    dp[i][i] = A[i]
    dp[i][(i+1)%N] = max(A[i], A[(i+1)%N])

for h in range(2, N):
    for i in range(N):
        j = (i+h) % N
        if A[(i+1)%N] > A[j]:
            tmp1 = A[i] + dp[(i+2)%N][j]
        else:
            tmp1 = A[i] + dp[(i+1)%N][(j-1)%N]
        if A[i] > A[(j-1)%N]:
            tmp2 = A[j] + dp[(i+1)%N][(j-1)%N]
        else:
            tmp2 = A[j] + dp[i][(j-2)%N]
        dp[i][j] = max(tmp1, tmp2)

ans = max([dp[i][(i-1)%N] for i in range(N)])
print(ans)



