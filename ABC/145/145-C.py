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

from itertools import permutations
N = ii()
xy = li2(N)
ans = float('inf')
tmp = 0.0
for l in permutations([i for i in range(N)]):
    for i in range(N-1):
        tmp += (pow(xy[l[i+1]][0]-xy[l[i]][0], 2) + pow(xy[l[i+1]][1]-xy[l[i]][1], 2))**0.5

bunshi = 1
for i in range(1, N+1):
    bunshi *= i
    
print(tmp / bunshi)