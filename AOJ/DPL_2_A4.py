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

## DP

N, E = mi()
rel = [[] for _ in range(N)]
#D = dp2(float('inf'), N, N)
for i in range(E):
    s, t, c = mi()
    rel[t].append([s, c])
    #D[s][t] = c

B = 1<<N

dp = dp2(float('inf'), N, B)
for i in range(N):
    dp[0][i] = 0
#dp[0][0] = 0

for i in range(B):
    for j in range(N):
        if dp[i][j] != float('inf'):
            #for v in range(N):
                #if D[j][v] != float('inf') and (not i & 1<<v):
                    #dp[i|1<<v][v] = min(dp[i|1<<v][v], dp[i][j]+D[j][v])
            for v in rel[j]:
                t, c = v[0], v[1]
                if not i & 1<<t:
                    dp[i|1<<t][t] = min(dp[i|1<<t][t], dp[i][j]+c)

#ans = min(dp[B-1])
ans = dp[B-1][0]

if ans == float('inf'):
    print(-1)
else:    
    print(ans)