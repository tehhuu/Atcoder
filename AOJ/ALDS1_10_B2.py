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

## 2次元DP

N = ii()
l = li2(N)

dp = dp2(float('inf'), N, N)

for i in range(N):
    dp[i][i] = 0

for h in range(1, N):
    for i in range(N):
        if i+h < N:
            if h == 1:
                dp[i][i+h] = l[i][0] * l[i][1] * l[i+h][1]
            else:
                for r in range(i, i+h):
                    dp[i][i+h] = min(dp[i][i+h], dp[i][r]+dp[r+1][i+h]+l[i][0]*l[r+1][0]*l[i+h][1])

print(dp[0][N-1])

'''
## 前から再起
dp = dp2(float('inf'), N, N)

def rec(h):
    if h == N+1:
        return
    if h == 0:
        for i in range(N):
            dp[i][i] = 0
    for i in range(N):
        if i+h < N:
            if h == 1:
                dp[i][i+h] = l[i][0] * l[i][1] * l[i+h][1]
            else:
                for r in range(i, i+h):
                    dp[i][i+h] = min(dp[i][i+h], dp[i][r]+dp[r+1][i+h]+l[i][0]*l[r+1][0]*l[i+h][1])
    rec(h+1)

rec(0)
print(dp[0][N-1])
'''
            

    
