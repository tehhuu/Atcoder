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

# square869120Contest #1 G
## メモ化再帰

N, M = mi()
if N==1:
    print(0, 1)
    exit()
rel = [[] for _ in range(N)]

for i in range(M):
    s, t, c, lim = mi()
    s, t = s-1, t-1
    rel[s].append((t, c, lim))
    rel[t].append((s, c, lim))

B = 2**N
dp = dp2(-1, N, B)
cnt = dp2(0, N, B)
cnt[0][0] = 1

def rec(state, now):
    if dp[state][now] != -1:
        return dp[state][now]
    if state == 0:
        dp[state][now] = 0
        return 0
    res = float('inf')
    for pv, c, lim in rel[now]:
        if pv==0 and state!=1:
            continue
        if state & 1<<pv and rec(state^(1<<pv), pv)+c <= lim:
            if res == rec(state^(1<<pv), pv)+c:
                cnt[state][now] += cnt[state^(1<<pv)][pv]
            if res > rec(state^(1<<pv), pv)+c:
                res = rec(state^(1<<pv), pv)+c
                cnt[state][now] = cnt[state^(1<<pv)][pv]
    dp[state][now] = res
    return res

ans = rec(B-1, 0)
#print(dp)
if ans == float('inf'):
    print('IMPOSSIBLE')
    exit()
print(ans, cnt[B-1][0])





