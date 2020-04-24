import sys
sys.setrecursionlimit(10**8)
def ii(): return int(sys.stdin.readline())
def mi(): return map(int, sys.stdin.readline().split())
def ti(): return tuple(map(int, sys.stdin.readline().split()))
def li2(N): return [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
def dp2(ini, i, j): return [[ini]*i for _ in range(j)]
def dp3(ini, i, j, k): return [[[ini]*i for _ in range(j)] for _ in range(k)]
#import bisect #bisect.bisect_left(B, a)
#from collections import defaultdict #d = defaultdict(int) d[key] += value
#from itertools import accumulate #list(accumulate(A))

## メモ化再帰
# TLE

def rec(i, j):
    if dp[i][j] != -1:
        return dp[i][j]
    if i == j:
        dp[i][j] = 0
        return 0
    if i+1 == j:
        if abs(A[i]-A[j]) < 2:
            dp[i][j] = 2
        else:
            dp[i][j] = 0
        return dp[i][j]
    if j - i:
        if abs(A[i]-A[j]) < 2 and rec(i+1, j-1) == j-i-1:
            dp[i][j] = j-i+1
        else:
            dp[i][j] = max([rec(i, k)+rec(k+1, j) for k in range(i, j)])
        return dp[i][j]
    dp[i][j] = max(rec(i+1, j), rec(i, j-1))
    return dp[i][j]

while True:
    N = ii()
    if N == 0:
        exit()
    A = ti()
    dp = dp2(-1, N, N)
    print(rec(0, N-1))

            




