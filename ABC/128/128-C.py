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

## bit全探索

from itertools import product

N, M = mi()
ks = []
for i in range(M):
    a = li()
    ks.append(a)
P = li()

cnt = 0

#for i in range(2**N):
    #x = bin(i)[2:].zfill(N)
    #l = list(map(int, list(x)))
for l in product([0, 1], repeat=N):
    for i in range(M):
        num , *switches = ks[i]
        if sum([l[sw-1] for sw in switches]) % 2 != P[i]:
            break
    else:
        cnt += 1

print(cnt)

    
