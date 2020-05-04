import sys
sys.setrecursionlimit(10**8)
def ii(): return int(sys.stdin.readline())
def mi(): return map(int, sys.stdin.readline().split())
def li(): return list(map(int, sys.stdin.readline().split()))
def li2(N): return [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
def dp2(ini, i, j): return [[ini]*i for _ in range(j)]
def dp3(ini, i, j, k): return [[[ini]*i for _ in range(j)] for _ in range(k)]
import bisect #bisect.bisect_left(B, a)
from collections import defaultdict #d = defaultdict(int) d[key] += value
#from itertools import accumulate #list(accumulate(A))


N = ii()
A = [ii() for _ in range(N)]

## 二分探索
B = sorted(list(set(A)))
for a in A:
    print(bisect.bisect_left(B, a))

'''
## 辞書用いた解法
d = defaultdict(int)
for i, b in enumerate(B):
    d[b] = i
for a in A:
    print(d[a])
'''
