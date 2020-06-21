import sys
sys.setrecursionlimit(10**8)
def ii(): return int(sys.stdin.readline())
def mi(): return map(int, sys.stdin.readline().split())
def li(): return list(map(int, sys.stdin.readline().split()))
def li2(N): return [list(map(int, sys.stdin.readline().split())) for i in range(N)]
def dp2(ini, i, j): return [[ini]*i for i2 in range(j)]
#import bisect #bisect.bisect_left(B, a)
from collections import defaultdict #d = defaultdict(int) d[key] += value
#from collections import Counter # a = Counter(A).most_common()
#from itertools import accumulate #list(accumulate(A))

N = ii()
A = li()
Q = ii()
B = li2(Q)

a = defaultdict(int)
for num in A:
    a[num] += 1

ans = sum(A)
for i in range(Q):
    if a[B[i][0]]:
        ans += (B[i][1]-B[i][0]) * a[B[i][0]]
        a[B[i][1]] += a[B[i][0]]
        a[B[i][0]] = 0
        print(ans)
    else:
        print(ans)