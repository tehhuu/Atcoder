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
## 3次元DP

N, K = mi()
l = [-1 for _ in range(N)]

for i in range(K):
    a, b = mi()
    l[a-1] = b-1

dp = dp3(0, 2, 3, N)

if l[0] != -1:
    dp[0][l[0]][0] = 1
else:
    for i in range(3):
        dp[0][i][0] = 1

for i in range(N-1):
    if l[i+1] != -1:
        for j in range(3):
            if j != l[i+1]:
                dp[i+1][l[i+1]][0] += sum(dp[i][j])
            else:
                dp[i+1][l[i+1]][1] += dp[i][l[i+1]][0]
    else:
        for j in range(3):
            for x in range(3):
                if j != x:
                    dp[i+1][j][0] += sum(dp[i][x])
                else:
                    dp[i+1][j][1] += dp[i][j][0]

ans = 0
for j in range(3):
    ans = (ans + sum(dp[N-1][j])) % 10000
print(ans)
