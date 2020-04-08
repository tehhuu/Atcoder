import sys
def ii(): return int(sys.stdin.readline())
def mi(): return map(int, sys.stdin.readline().split())
def li(): return list(map(int, sys.stdin.readline().split()))
def li2(N): return [list(map(int, sys.stdin.readline().split())) for i in range(N)]
def dp2(ini, i, j): return [[ini]*i for i2 in range(j)]
def dp3(ini, i, j, k): return [[[ini]*i for i2 in range(j)] for i3 in range(k)]
#import bisect #bisect.bisect_left(B, a)
#from collections import defaultdict #d = defaultdict(int) d[key] += value

'''
### TLE
from collections import deque
N, M = mi()
x = li2(M)

#dp = dp2(0, 2, N)
dp = [[0, []] for i1 in range(N+1)]

tmp = deque([])

for i in range(M):
    dp[x[i][1]][0] = max(dp[x[i][1]][0], dp[x[i][0]][0] + 1)
    dp[x[i][0]][1].append(x[i][1])
    tmp.append(x[i][1])
    while tmp != deque():
        a = tmp.popleft()
        if dp[a][1] != []:
            for b in dp[a][1]:
                dp[b][0] = max(dp[a][0] + 1, dp[b][0])
                tmp.append(b)

print(max([row[0] for row in dp])) 
'''

### BFSトポロジカルソート + DP

from collections import deque

## 入力受け取り
N, M = mi()
x = li2(M)

## 隣接リスト & 入次数リスト作成
h = [0]*N
adj = [[] for i in range(N)]
for i in range(M):
    x[i][0] -= 1
    x[i][1] -= 1
    h[x[i][1]] += 1
    adj[x[i][0]].append(x[i][1])

## 入次数0のものを事前に格納
zeros = deque([])
#ans = []
for i in range(N):
    if h[i] == 0:
        zeros.append(i)
        #ans.append(i)


## BFSトポロジカルソート & DP
dp = [0]*N

while(zeros != deque()):
    a = zeros.popleft()
    if(adj[a]):
        for b in adj[a]:
            h[b] -= 1
            if h[b] == 0:
                zeros.append(b)
                dp[b] = max(dp[a] + 1, dp[b])
                #ans.append(b)
'''
dp = [0]*N
for a in ans:
    if adj[a]:
        for b in adj[a]:
            dp[b] = max(dp[a] + 1, dp[b])

print(dp[ans[-1]])
'''
print(max(dp))