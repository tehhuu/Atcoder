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

N = ii()
S = [input() for _ in range(2)]

mod = 10**9+7
pat = []
i = 0
ans = 1
while i < N:
    if S[0][i] == S[1][i]:
        if i > 0:
            if pat[-1] == 0:
                ans = (ans * 2) % mod
        else:
            ans *= 3
        pat.append(0)
        i += 1
    else:
        if i > 0:
            if pat[-1] == 0:
                ans = (ans * 2) % mod
            else:
                ans = (ans * 3) % mod
        else:
            ans *= 6
        pat.append(1)
        i += 2

print(ans)