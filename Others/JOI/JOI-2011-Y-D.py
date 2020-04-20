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

## 2011 JOI 予選　D

N = ii()
*A, ans = mi()

dp = dp2(0, N, 21)
dp[0][0] = 1

for j in range(1, N):
    for i in range(21):
        if dp[i][j-1] != 0:
            if i + A[j-1] < 21:
                dp[i+A[j-1]][j] += dp[i][j-1]
            if i - A[j-1] >= 0:
                dp[i-A[j-1]][j] += dp[i][j-1]

print(dp[ans][N-1])
