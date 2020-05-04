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

## bit　全探索

from itertools import product

N, M = mi()
xy = li2(M)

ans = 0
for l in product([0, 1], repeat=N):
    flag = 1
    cnt = 0
    for x, y in xy:
        if l[x-1] == l[y-1] == 1:
            cnt += 2
    sum_l = sum(l)
    if cnt == sum_l * (sum_l - 1):
        ans = max(ans, sum_l)

print(ans)