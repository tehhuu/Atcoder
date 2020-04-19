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

## メモ化再帰-3
N, E = mi()
rel = [[] for _ in range(N)]
#D = dp2(float('inf'), n, n)
for i in range(E):
    s, t, c = mi()
    rel[t].append([s, c])

B = 1<<N
dp = dp2(float("inf"), N, B)
flag = dp2(0, N, B)

def rec(state, now):
    if flag[state][now]:
        return dp[state][now]
    if state == B-1 and now == 0:
        dp[B-1][0] = 0
        return 0
    for r in rel[now]:
        t, c = r[0], r[1]
        if not state & (1<<t):
            dp[state][now] = min(rec(state|(1<<t),t)+c, dp[state][now])
    flag[state][now] = 1
    return dp[state][now]

ans = rec(0, 0)

if ans == float('inf'):
    print(-1)
else:    
    print(ans)