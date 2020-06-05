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

N, M = mi()
rel = [[] for _ in range(N)]

for _ in range(M):
    a, b = mi()
    a, b = a-1, b-1
    rel[a].append(b)
    rel[b].append(a)

for i in range(N):
    cnt = set()
    for j in rel[i]:
        for k in rel[j]:
            if k != i and k not in rel[i]:
                cnt.add(k)
    print(len(cnt))