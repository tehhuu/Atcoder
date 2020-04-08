import sys 
def ii(): return int(sys.stdin.readline())
def mi(): return map(int, sys.stdin.readline().split())
def li(): return list(map(int, sys.stdin.readline().split()))
def li2(N): return [list(map(int, sys.stdin.readline().split())) for i in range(N)]
def dp2(ini, i, j): return [[ini]*i for i2 in range(j)]
def dp3(ini, i, j, k): return [[[ini]*i for i2 in range(j)] for i3 in range(k)]
#import bisect #bisect.bisect_left(B, a)
#from collections import defaultdict #d = defaultdict(int) d[key] += value

### DFSトポロジカルソート + DP

from collections import deque
sys.setrecursionlimit(10**6)

#DFS
def dfs(x):
    if flag[x]:
        return
    else:
        flag[x] = 1
        for a in adj[x]:
            dfs(a)
        global ans
        ans.appendleft(x)

#入力受け取り
N, M = mi()
x = li2(M)

#隣接リスト作成
adj = [[] for i in range(N)]
for i in range(M):
    x[i][0] -= 1
    x[i][1] -= 1
    adj[x[i][0]].append(x[i][1])

#DFSを利用したトポロジカルソート
flag = [0]*N
ans = deque([])
for i in range(N):
    dfs(i)

## DP
dp = [0]*N
for a in ans:
    for b in adj[a]:
        dp[b] = max(dp[b], dp[a] + 1)

print(max(dp))





