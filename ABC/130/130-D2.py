import sys
sys.setrecursionlimit(10**8)
def ii(): return int(sys.stdin.readline())
def mi(): return map(int, sys.stdin.readline().split())
def li(): return list(map(int, sys.stdin.readline().split()))
def li2(N): return [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
def dp2(ini, i, j): return [[ini]*i for _ in range(j)]
def dp3(ini, i, j, k): return [[[ini]*i for _ in range(j)] for _ in range(k)]
import bisect #bisect.bisect_left(B, a)
#from collections import defaultdict #d = defaultdict(int) d[key] += value
from itertools import accumulate #list(accumulate(A))

N, K = mi()
A = li()
ans = 0

wa = list(accumulate(A))
if wa[N-1] < K:
    print(0)
    exit()

ind = bisect.bisect_left(wa, K)
ans += N - ind

for i in range(1, N):
    ind = bisect.bisect_left(wa, K+wa[i-1])
    if ind == N-1 and wa[ind]-wa[i-1] < K:
        continue
    ans += N - ind

print(ans)