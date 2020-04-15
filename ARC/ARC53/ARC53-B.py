import sys
sys.setrecursionlimit(10**8)
def ii(): return int(sys.stdin.readline())
def mi(): return map(int, sys.stdin.readline().split())
def li(): return list(map(int, sys.stdin.readline().split()))
def li2(N): return [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
def dp2(ini, i, j): return [[ini]*i for _ in range(j)]
def dp3(ini, i, j, k): return [[[ini]*i for _ in range(j)] for _ in range(k)]
#import bisect #bisect.bisect_left(B, a)
from collections import defaultdict #d = defaultdict(int) d[key] += value
#from itertools import accumulate #list(accumulate(A))

S = input()
d = defaultdict(int)

for m in S:
    d[m] += 1

p_cnt = 0
n_cnt = 0

for v in d.values():
    p_cnt += v // 2
    n_cnt += v % 2

if n_cnt == 0:
    print(p_cnt*2)
else:
    print(1 + 2*(p_cnt//n_cnt))

     