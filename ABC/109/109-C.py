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

H, W = mi()
S = [li() for _ in range(H)]
f = 0
ans = []

for j in range(W):
    for i in range(H):
        if j%2:
            i = (H-1) - i
        if f:
            ans.append([pi, pj, i+1, j+1])
        if S[i][j] % 2:
            f = 1 - f
        pi, pj = i+1, j+1

N = len(ans)
print(N)
for i in range(N):
    print(ans[i][0], ans[i][1], ans[i][2], ans[i][3])




