import sys
sys.setrecursionlimit(10**8)
def ii(): return int(sys.stdin.readline())
def mi(): return map(int, sys.stdin.readline().split())
def li(): return list(map(int, sys.stdin.readline().split()))
def li2(N): return [list(map(int, sys.stdin.readline().split())) for i in range(N)]
def dp2(ini, i, j): return [[ini]*i for i2 in range(j)]
def dp3(ini, i, j, k): return [[[ini]*i for i2 in range(j)] for i3 in range(k)]
import bisect #bisect.bisect_left(B, a)
#from collections import defaultdict #d = defaultdict(int) d[key] += value
#from collections import Counter # a = Counter(A).most_common()
#from itertools import accumulate #list(accumulate(A))

N = ii()
A = li()

A_r = [A[i]-(i+1) for i in range(N)]
B = sorted(A_r)

cnt = 0
for i in range(N):
    num = -2*(i+1)-A_r[i]
    ind_l = bisect.bisect_left(B, num)
    if B[ind_l] != num:
        continue
    ind_r = bisect.bisect_right(B, num)
    cnt += ind_r - ind_l

print(cnt)