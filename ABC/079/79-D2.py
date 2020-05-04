import sys
sys.setrecursionlimit(10**9)
def ii(): return int(sys.stdin.readline())
def mi(): return map(int, sys.stdin.readline().split())
def li(): return list(map(int, sys.stdin.readline().split()))
def li2(N): return [list(map(int, sys.stdin.readline().split())) for i in range(N)]
def dp2(ini, i, j): return [[ini]*i for i2 in range(j)]
def dp3(ini, i, j, k): return [[[ini]*i for i2 in range(j)] for i3 in range(k)]
#import bisect #bisect.bisect_left(B, a)
#from collections import defaultdict #d = defaultdict(int) d[key] += value

from collections import deque

H, W = mi()
C = li2(10)
a = li2(H)

## 1までの最小コストを記憶
memo = [C[i][1] for i in range(10)]

## BFS
for i in range(10):
    que = deque()
    lim = C[i][1]
    for j in range(10):
        if C[i][j] < lim:
            que.append([j, C[i][j]])
    while que != deque():
        k = que.popleft()
        for j in range(10):
            if C[k[0]][j] + k[1] < lim and k[0] != j:
                if j == 1:
                    memo[i] = min(memo[i], C[k[0]][j] + k[1])
                else:
                    que.append([j, C[k[0]][j] + k[1]])

## 各要素における最小コストを合計
ans = 0
for i in range(H):
    for j in range(W):
        if abs(a[i][j]) != 1:
            ans += memo[a[i][j]]

print(ans)


    
