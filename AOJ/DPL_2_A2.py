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

## メモ化再帰-2
N, E = mi()
rel = [[] for _ in range(N)]
for i in range(E):
    s, t, c = mi()
    rel[t].append([s, c])

B = 1<<N
dp = dp2(-1, N, B)

def rec(state, now):
    if dp[state][now] != -1:
        return dp[state][now]
    if state == B-1 and now == 0:
        dp[B-1][0] = 0
        return 0
    res = float("inf")
    for r in rel[now]:
        t, c = r[0], r[1]
        if not state & (1<<t):
        #if not (state>>t)&1:
            if res > rec(state|(1<<t), t) + c:
                res = rec(state|(1<<t), t) + c
    dp[state][now] = res
    return res

ans = rec(0, 0)
print(dp)
if ans == float('inf'):
    print(-1)
else:    
    print(ans)