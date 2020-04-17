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

## DFS

'''
## DFS 別解
N, M = mi()
xy = li2(M)

pat = [0]*N
ans = 0
def dfs(pat, pos):
    if pos == N:
        cnt = 0
        for x, y in xy:
            if pat[x-1] == pat[y-1] == 1:
                cnt += 2
        sum_pat = sum(pat)
        if cnt == sum_pat * (sum_pat - 1):
            global ans
            ans = max(ans, sum_pat)
    else:
        pat[pos] = 0
        dfs(pat, pos+1)
        pat[pos] = 1
        dfs(pat, pos+1)

dfs(pat, 0)
print(ans)
'''

N, M = mi()
rel = dp2(0, N+1, N+1)

for i in range(M):
    x, y = mi()
    x, y = x-1, y-1
    rel[x][y] = rel[y][x] = 1

ans = 0
def dfs(l, pos=0):
    if pos == N:
        len_l = len(l)
        for i in range(len_l):
            for j in range(i+1, len_l):
                if rel[l[i]][l[j]] != 1:
                    return
        global ans
        ans = max(ans, len_l)
    else:
        dfs(l, pos+1)
        l.append(pos)
        dfs(l, pos+1)
        l.pop(-1)

v = []
dfs(v)
print(ans)
