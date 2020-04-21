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

## 2012 JOI 予選　D
## 3×3の二次元DP

N, K = mi()
l = [0 for _ in range(N)]

for i in range(K):
    a, b = mi()
    l[a-1] = b

dp = dp2(0, 4, 3)

if l[0]:
    dp[0][l[0]] = 1
else:
    for i in range(1, 4):
        dp[0][i] = 1
if l[1]:
    dp[1][l[1]] = sum(dp[0])
else:
    for i in range(1, 4):
        dp[1][i] = sum(dp[0])

for i in range(2, N):
    for j in range(1, 4):
        dp[i%3][j] = 0
    if l[i]:
        for j in range(1, 4):
            if j != l[i]:
                dp[i%3][l[i]] += dp[(i-1)%3][j]
                if dp[(i-1)%3][l[i]] != 0:
                    dp[i%3][l[i]] += dp[(i-2)%3][j]
    else:
        for j in range(1, 4):
            for x in range(1, 4):
                if j != x:
                    dp[i%3][j] += dp[(i-1)%3][x]
                    if dp[(i-1)%3][j] != 0:
                        dp[i%3][j] += dp[(i-2)%3][x]
cnt = 0
for i in range(1, 4):
    cnt = (cnt + dp[(N-1)%3][i]) % 10000
print(cnt)
                
