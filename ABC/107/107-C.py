import sys
def ii(): return int(sys.stdin.readline())
def mi(): return map(int, sys.stdin.readline().split())
def li(): return list(map(int, sys.stdin.readline().split()))
def li2(N): return [list(map(int, sys.stdin.readline().split())) for i in range(N)]
def dp2(ini, i, j): return [[ini]*i for i2 in range(j)]
def dp3(ini, i, j, k): return [[[ini]*i for i2 in range(j)] for i3 in range(k)]
#import bisect #bisect.bisect_left(B, a)
#from collections import defaultdict #d = defaultdict(int) d[key] += value

N, K = mi()
x = li()
ans = 10**13 + 1

for i in range(N-K+1):
    sum_k = x[K-1+i] - x[i] + min(abs(x[i]), abs(x[K-1+i]))
    ans = min(ans, sum_k)

print(ans)


