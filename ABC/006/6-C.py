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

sum_xy = 4 * N - M

if sum_xy < 0:
    print(-1, -1, -1)
    exit()

if sum_xy % 2:
    y = 1
    x = (sum_xy - 1) //2
    z = N - x - y
else:
    y = 0
    x = sum_xy //2
    z = N - x - y

if z < 0:
    print(-1, -1, -1)
    exit()
print(x, y, z)