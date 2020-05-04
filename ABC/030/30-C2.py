import sys
sys.setrecursionlimit(10**8)
def ii(): return int(sys.stdin.readline())
def mi(): return map(int, sys.stdin.readline().split())
def li(): return list(map(int, sys.stdin.readline().split()))
def li2(N): return [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
def dp2(ini, i, j): return [[ini]*i for _ in range(j)]
def dp3(ini, i, j, k): return [[[ini]*i for _ in range(j)] for _ in range(k)]
from bisect import bisect_right, bisect_left #bisect_left(B, a)
#from collections import defaultdict #d = defaultdict(int) d[key] += value
#from itertools import accumulate #list(accumulate(A))

## 前向き探索

N, M = mi()
x, y = mi()
A = li()
B = li()

ind_a = ind_b = 0
cnt = 0
while True:
    ind_b = bisect_left(B, A[ind_a]+x, ind_b, M)
    if ind_b == M:
        break
    cnt += 1
    ind_a = bisect_left(A, B[ind_b]+y, ind_a, N)
    if ind_a == N:
        break

print(cnt)