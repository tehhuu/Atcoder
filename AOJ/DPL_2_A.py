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

## メモ化再帰-1
n, E = mi()
#rel = [[] for _ in range(n)]
D = dp2(float('inf'), n, n)
for i in range(E):
    s, t, c = mi()
    #rel[t].append([s, c])
    D[s][t] = c

B = 1<<n
#dp = dp2(float('inf'), n, B)
dp = dp2(-1, n, B)
dp[0][0] = 0

def rec(g, now):
    #if dp[g][now] != float('inf'):
    if dp[g][now] != -1:   
        return dp[g][now]
    prev_g = g & ~(1<<now)
    if prev_g == 0:
        dp[now][now] = D[0][now]
        return dp[now][now]
    #if g==0:
        #return dp[0][0]
    res = float('inf')
    for i in range(n):
        if not (prev_g & (1<<i)):
            continue
        if res > rec(prev_g, i) + D[i][now]:
            res = rec(prev_g, i) + D[i][now]
        #dp[g][now] = min(rec(prev_g, i)+D[i][now], dp[g][now])
    dp[g][now] = res
    return dp[g][now]

ans = rec(B-1, 0)
print(dp)
if ans == float('inf'):
    print(-1)
else:    
    print(ans)

'''
## DFS全探索(TLE)
V, E = mi()
rel = [[] for _ in range(V)]
for i in range(E):
    s, t, d = mi()
    rel[s].append([d, t])

ans = float('inf')
def dfs(s, pos, d, used):
    if s==pos and d!=0:
        global ans
        if sum(used) == V-1:
            ans = min(ans, d)
            #print(s, d, used)
        return
    else:
        #print(s, pos, d, used, keiro)
        for v in rel[pos]:
            if not used[v[1]]:
                if v[1]!= s:
                    used[v[1]] = 1
                #print(s, v[1], d, v[0], used, keiro)
                dfs(s, v[1], d+v[0], used)
                if v[1]!= s:
                    used[v[1]] = 0

#for i in range(V):
flag = [0]*V
dfs(0, 0, 0, flag)

if ans == float('inf'):
    print(-1)
else:
    print(ans)
'''