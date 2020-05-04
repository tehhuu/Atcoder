import sys
sys.setrecursionlimit(10**8)
def ii(): return int(sys.stdin.readline())
def mi(): return map(int, sys.stdin.readline().split())
def li(): return list(map(int, sys.stdin.readline().split()))
def li2(N): return [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
def dp2(ini, i, j): return [[ini]*i for _ in range(j)]
def dp3(ini, i, j, k): return [[[ini]*i for _ in range(j)] for _ in range(k)]
from bisect import bisect_right, bisect_left #bisect_left(B, a)
#from collections import defaultdict #d = defaultdict(int) d[key] += value
#from itertools import accumulate #list(accumulate(A))

'''
# leftとrightで挙動が違うことで少し手間取った
A = [20, 22, 24, 28, 33]
print(bisect_right(A, 33))
print(bisect_left(A, 33))
'''

## 後ろ向き探索

N, M = mi()
x, y = mi()
A = li()
B = li()
ind_b = M-1
ind_a = bisect_right(A, B[ind_b]-x) - 1
if ind_a >= 0:
    cnt = 1
else:
    print(0)
    exit()
while True:
    ind_b = bisect_right(B, A[ind_a]-y, 0, ind_b) - 1
    if ind_b < 0:
        break
    ind_a = bisect_right(A, B[ind_b]-x, 0, ind_a) - 1
    if ind_a < 0:
        break
    cnt += 1

print(cnt)