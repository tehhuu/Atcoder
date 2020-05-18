import sys
sys.setrecursionlimit(10**8)
def ii(): return int(sys.stdin.readline())
def mi(): return map(int, sys.stdin.readline().split())
def li(): return list(map(int, sys.stdin.readline().split()))
def li2(N): return [list(map(int, sys.stdin.readline().split())) for i in range(N)]
def dp2(ini, i, j): return [[ini]*i for i2 in range(j)]
def dp3(ini, i, j, k): return [[[ini]*i for i2 in range(j)] for i3 in range(k)]
#import bisect #bisect.bisect_left(B, a)
#from collections import defaultdict #d = defaultdict(int) d[key] += value
#from collections import Counter # a = Counter(A).most_common()
#from itertools import accumulate #list(accumulate(A))
import math

A, B, H, M = mi()

M_ratio = (M * 12 /60) /12
H_ratio = H / 12 + M_ratio / 12

k = 360 * abs(H_ratio - M_ratio)
k = min(k, 360-k)
k = math.radians(k)

print(math.sqrt(A**2+B**2-(2*A*B)*math.cos(k)))
