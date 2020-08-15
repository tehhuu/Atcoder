import sys
sys.setrecursionlimit(10**8)
def ii(): return int(sys.stdin.readline())
def mi(): return map(int, sys.stdin.readline().split())
def li(): return list(map(int, sys.stdin.readline().split()))
def li2(N): return [list(map(int, sys.stdin.readline().split())) for i in range(N)]
def dp2(ini, i, j): return [[ini]*i for i2 in range(j)]
#import bisect #bisect.bisect_left(B, a)
#from collections import defaultdict #d = defaultdict(int) d[key] += value
#from collections import Counter # a = Counter(A).most_common()
#from itertools import accumulate #list(accumulate(A))
from itertools import combinations

N = ii()
A = li()
cnt = 0

for c in combinations(A, 3):
    c = sorted(c)
    if c[0] != c[1] and c[1] != c[2]:
        if c[0] + c[1] > c[2]:
            cnt += 1

print(cnt)